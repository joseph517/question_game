from rest_framework import serializers
from apps.questions.models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'