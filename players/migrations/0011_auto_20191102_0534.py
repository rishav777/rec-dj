# Generated by Django 2.2.5 on 2022-11-02 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_auto_20221101_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.ManyToManyField(blank=True, related_name='player_positions', to='players.Positions'),
        ),
    ]
