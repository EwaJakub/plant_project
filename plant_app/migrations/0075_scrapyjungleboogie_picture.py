# Generated by Django 3.2.9 on 2022-03-31 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0074_remove_scrapyjungleboogie_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapyjungleboogie',
            name='picture',
            field=models.TextField(blank=True),
        ),
    ]
