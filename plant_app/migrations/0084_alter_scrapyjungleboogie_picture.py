# Generated by Django 3.2.9 on 2022-04-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0083_auto_20220401_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapyjungleboogie',
            name='picture',
            field=models.TextField(blank=True),
        ),
    ]