# Generated by Django 3.2.9 on 2022-03-17 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0028_plant_direction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='direction',
        ),
    ]
