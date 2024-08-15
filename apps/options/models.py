from django.db import models

# Create your models here.
class Option(models.Model):
    question = models.ForeignKey('questions.Question', related_name='options', on_delete=models.CASCADE)
    option = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)