# Generated by Django 2.2.5 on 2022-11-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0006_school_logo'),
        ('players', '0021_positions_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolsVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schools', models.ManyToManyField(blank=True, related_name='schools_visit', to='address.School')),
            ],
        ),
    ]
