from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Question

# Register your models here.


@register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = (
        'game',
        'question',
        'score',
    )
    list_filter = (
        'game',
    )

