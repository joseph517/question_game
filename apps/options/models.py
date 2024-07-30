from django.db import models

# Create your models here.
class Option(models.Model):
    question = models.ForeignKey('questions.Question', on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    is_correct = models.BooleanField(default=False)