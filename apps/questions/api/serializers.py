from rest_framework import serializers
from apps.games.models import Game
from apps.questions.models import *
from apps.options.api.serializers import OptionSerializer

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name_game']

class QuestionSerializer(serializers.ModelSerializer):

    options = OptionSerializer(many=True, read_only=True)
    game = GameSerializer(read_only=True)
    

    class Meta:
        model = Question
        fields = '__all__'


class QuestionsCreateSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

class validateAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField()


