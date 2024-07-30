from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.options.api.serializers import OptionSerializer
from apps.options.models import Option

#views to options services

class CreateOptionService(generics.CreateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateOptionService(generics.UpdateAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put (self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class DeleteOptionService(generics.DestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

class ListOptionService(generics.ListAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAuthenticated]