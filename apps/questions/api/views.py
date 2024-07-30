from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.questions.api.serializers import QuestionSerializer
from apps.questions.models import Question

#views to questions services

class CreateQuestionService(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateQuestionService(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put (self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class DeleteQuestionService(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

class ListQuestionService(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]