# Generated by Django 3.2.9 on 2022-03-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0049_scrapyjungleboogie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapyjungleboogie',
            name='link',
            field=models.TextField(blank=True),
        ),
    ]
