from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.options.models import Option
from apps.questions.api.serializers import QuestionSerializer, validateAnswerSerializer
from apps.questions.models import Question
from rest_framework.response import Response
from apps.games.models import Game, UserGame


#views to questions services

class CreateQuestionView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class UpdateQuestionView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def put (self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class DeleteQuestionView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

class ListQuestionByGame(generics.ListAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        game_id = self.kwargs.get('game_id')
        game = Game.objects.get(id=game_id)
        user_game, created = UserGame.objects.get_or_create(user=self.request.user, game=game)           
        return self.queryset.filter(game=game_id).exclude(id__in=user_game.answered_questions.all().values_list('id', flat=True))
    
class ListQuestionView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class ValidateAnswerView(generics.GenericAPIView):
    serializer_class = validateAnswerSerializer
    permission_classes = [IsAuthenticated]


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