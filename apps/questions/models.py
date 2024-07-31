from django.db import models

from apps.options.models import Option
 

# Create your models here.

class Question(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.question
    
# class QuestionValidator:

#     response = models.CharField(max_length=100)

#     def __init__(self, user, game):
#         self.user = user
#         self.game = game
#         self.total_score = 0

#     def validate_option(self, option_id):
#         option = Option.objects.get(pk=option_id)
#         if option.is_correct:
#             self.game.total_score += option.question.score
#             self.game.save()
#         return option.is_correct

#     def get_total_score(self):
#         return self.total_scoreo