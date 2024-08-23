from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from apps.games.api.serializers import GameSerializer, UserGameSerializer
from apps.games.models import Game, UserGame
from apps.users.models import User

#views to games services

class CreateGameView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateGameView(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put (self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class DeleteGameView(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

class ListGameView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.queryset.all()
        return self.queryset.filter(user_games__user=user)


class RankingGameView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, game_id):
        try:
            game = Game.objects.get(id=game_id)
        except Game.DoesNotExist:
            return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)
        
        user_scores = UserGame.objects.filter(game=game).values('user__name', 'score').order_by('-score')
        
        return Response(user_scores, status=status.HTTP_200_OK)
    

class AssignGameToUserView(generics.CreateAPIView):
    serializer_class = UserGameSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        user_id = request.headers.get('user_id')
        game_id = request.headers.get('game_id')

        if not user_id or not game_id:
            return Response({'error': 'Missing user_id or game_id'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
            game = Game.objects.get(id=game_id)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        except Game.DoesNotExist:
            return Response({'error': 'Game does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user already has the game assigned
        if UserGame.objects.filter(user=user, game=game).exists():
            return Response({'error': 'Game already assigned to user'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new UserGame object
        user_game = UserGame.objects.create(user=user, game=game)
        serializer = self.get_serializer(user_game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)