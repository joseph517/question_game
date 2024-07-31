from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.options.models import Option
from apps.questions.api.serializers import QuestionSerializer, validateAnswerSerializer
from apps.questions.models import Question
from rest_framework.response import Response
from apps.games.models import UserGame


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


class ValidateAnswerView(generics.GenericAPIView):
    serializer_class = validateAnswerSerializer
    # permission_classes = [IsAuthenticated]


    def post(self, request, *args, **kwargs):
        question_id = request.data.get('question_id')
        option_id = request.data.get('option_id')

        question = Question.objects.get(pk=question_id)
        option = Option.objects.get(pk=option_id)

        user_game, created = UserGame.objects.get_or_create(user=request.user, game=question.game)
        is_correct = user_game.validate_option(option)


        if is_correct:
            return Response({"message": "Respuesta correcta"})
        else:
            return Response({"message": "Respuesta incorrecta"})