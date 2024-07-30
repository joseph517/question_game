from django.contrib import admin
from django.contrib.admin import ModelAdmin, register
from .models import User

# Register your models here.
@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'password',
    )
    list_filter = (
        'name',
    )