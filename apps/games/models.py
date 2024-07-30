from django.db import models

# Create your models here.
class Game(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name_game = models.CharField(max_length=100)
    description = models.TextField()
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return self.name_game