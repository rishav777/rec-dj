# Generated by Django 2.2.5 on 2022-12-28 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0009_state_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]