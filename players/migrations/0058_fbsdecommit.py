# Generated by Django 2.2.5 on 2020-01-22 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0012_college'),
        ('players', '0057_auto_20200121_0312'),
    ]

    operations = [
        migrations.CreateModel(
            name='FbsDeCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decommited_on', models.CharField(blank=True, max_length=150, null=True)),
                ('school', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.School')),
            ],
        ),
    ]
