from rest_framework import serializers
from apps.questions.models import *
from apps.options.api.serializers import OptionSerializer

class QuestionSerializer(serializers.ModelSerializer):

    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

class validateAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField()