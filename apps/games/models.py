from django.db import models

# Create your models here.
class Game(models.Model):
    # users = models.ManyToManyField('users.User', through='UserGame', blank=True)
    name_game = models.CharField(max_length=100)
    description = models.TextField()

    def get_games_for_user(self, user):
        return self.usergame_set.filter(user=user).values_list('game', flat=True)

    def __str__(self):
        return self.name_game
    
class UserGame(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_games')
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE, related_name='user_games')
    score = models.IntegerField(default=0)
    answered_questions = models.ManyToManyField('questions.Question', blank=True, null=True)

    class Meta:
        unique_together = ('user', 'game')

    def validate_option(self, option):
        self.answered_questions.add(option.question.id)
        if option.is_correct:
            self.score += option.question.score
            self.save()
        return option.is_correct
        
