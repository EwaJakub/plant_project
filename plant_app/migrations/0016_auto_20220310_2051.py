# Generated by Django 3.2.9 on 2022-03-10 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0015_auto_20220310_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airpurifying',
            name='influence_data',
        ),
        migrations.RemoveField(
            model_name='airpurifying',
            name='influence_description',
        ),
        migrations.RemoveField(
            model_name='animalinfluence',
            name='influence_data',
        ),
        migrations.RemoveField(
            model_name='animalinfluence',
            name='influence_description',
        ),
    ]
