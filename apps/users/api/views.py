from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

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
            'access': str(access_token),
            'user_id': user.id,
            'rol': user.is_staff,
            'name': user.name
        }

        return Response(data)

class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer