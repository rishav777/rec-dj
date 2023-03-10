# Generated by Django 2.2.5 on 2020-01-09 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0053_player_video_highlight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('logo', models.FileField(blank=True, null=True, upload_to='Teams/')),
            ],
        ),
    ]
