# Generated by Django 2.2.5 on 2022-11-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0025_player_fbs_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='star_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
