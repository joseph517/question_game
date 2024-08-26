from django.db import models

from apps.options.models import Option
 

# Create your models here.

class Question(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.question