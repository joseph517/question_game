from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, DeleteUserSerializer, UserCreateSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404



from apps.users.models import User

class ObtainTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user

        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token

        data = {
            'refresh': str(refresh),
            'access_token': str(access_token),
            'user_id': user.id,
            'rol': user.is_staff,
            'name': user.name
        }

        return Response(data)

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer


class LogoutView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user_id', ))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Sesión cerrada correctamente'}, status=status.HTTP_200_OK)

        return Response({'message': 'Error al cerrar sesión'}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response("User created successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class DeleteUserView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = DeleteUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def delete(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(User, pk=kwargs['pk'])  # Buscar el usuario por ID
            user.delete()
            return Response({"message": "Usuario eliminado exitosamente", "email": user.email}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e), "message": "Error al eliminar el usuario"}, status=status.HTTP_400_BAD_REQUEST)