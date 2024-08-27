from rest_framework import serializers
from apps.games.models import *

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = ['id', 'user', 'game', 'score']

class ListGameByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name_game']