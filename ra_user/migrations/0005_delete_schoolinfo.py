# Generated by Django 2.2.5 on 2022-10-21 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ra_user', '0004_remove_user_school'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SchoolInfo',
        ),
    ]
