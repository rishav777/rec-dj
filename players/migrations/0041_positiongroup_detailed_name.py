# Generated by Django 2.2.5 on 2022-12-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0040_player_video_highlight'),
    ]

    operations = [
        migrations.AddField(
            model_name='positiongroup',
            name='detailed_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
