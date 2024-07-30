from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Game

# Register your models here.
@register(Game)
class GameAdmin(ModelAdmin):
    list_display = (
        'user',
        'name_game',
        'description',
        'total_score',
    )
    list_filter = (
        'name_game',
    )
