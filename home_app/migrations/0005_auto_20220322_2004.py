# Generated by Django 3.2.9 on 2022-03-22 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_rename_second_name_userprofile_surename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='surename',
        ),
    ]
