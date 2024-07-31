from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Game, UserGame

# Register your models here.
class UserGameAdmin(admin.ModelAdmin):
    list_display = (
        'game',
        'user',
        'score',
    )
    list_filter = (
        'game',
    )

class GameAdmin(admin.ModelAdmin):
    list_display = (
        'name_game',
        'description',
        'total_score',
    )
    list_filter = (
        'name_game',
    )

admin.site.register(UserGame, UserGameAdmin)
admin.site.register(Game, GameAdmin)