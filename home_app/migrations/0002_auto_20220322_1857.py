# Generated by Django 3.2.9 on 2022-03-22 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='my_plants',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='wish_list',
        ),
    ]
