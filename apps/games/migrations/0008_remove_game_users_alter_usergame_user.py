# Generated by Django 4.2.14 on 2024-08-22 21:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0007_alter_usergame_answered_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='users',
        ),
        migrations.AlterField(
            model_name='usergame',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
