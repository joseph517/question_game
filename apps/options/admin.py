from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import Option

# Register your models here.


@register(Option)
class OptionAdmin(ModelAdmin):
    list_display = (
        'question',
        'option',
        'is_correct',
    )
    list_filter = (
        'is_correct',
    )