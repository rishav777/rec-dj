# Generated by Django 2.2.5 on 2020-01-21 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0056_schoolsvisit_total_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='interception',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='sack',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='touchdown',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
