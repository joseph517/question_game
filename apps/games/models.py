from django.db import models

# Create your models here.
class Game(models.Model):
    users = models.ManyToManyField('users.User', through='UserGame')
    name_game = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name_game
    
class UserGame(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        unique_together = ('user', 'game')

    def validate_option(self, option):
        if option.is_correct:
            self.score += option.question.score
            self.save()
        return option.is_correct

        