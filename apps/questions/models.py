from django.db import models

# Create your models here.

class Question(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.question    