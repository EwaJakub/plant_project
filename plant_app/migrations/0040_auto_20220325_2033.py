# Generated by Django 3.2.9 on 2022-03-25 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0039_auto_20220325_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapyjungleboogie',
            name='link',
        ),
        migrations.RemoveField(
            model_name='scrapyjungleboogie',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='scrapyjungleboogie',
            name='price',
        ),
    ]
