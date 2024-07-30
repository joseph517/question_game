from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.games.api.serializers import GameSerializer
from apps.games.models import Game

#views to games services

class CreateGameService(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateGameService(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put (self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class DeleteGameService(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

class ListGameService(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]