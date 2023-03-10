# Generated by Django 2.2.5 on 2020-05-23 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0076_auto_20200522_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='savedsearch',
            options={'ordering': ('-searched_on',)},
        ),
        migrations.AddField(
            model_name='savedsearch',
            name='searched_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
