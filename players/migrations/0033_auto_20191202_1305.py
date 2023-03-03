# Generated by Django 2.2.5 on 2022-12-02 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('players', '0032_auto_20221202_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='player',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='player_notes', to='players.Notes'),
        ),
    ]
