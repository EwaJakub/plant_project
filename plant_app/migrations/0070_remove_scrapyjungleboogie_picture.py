# Generated by Django 3.2.9 on 2022-03-31 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0069_scrapyjungleboogie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapyjungleboogie',
            name='picture',
        ),
    ]