# Generated by Django 3.2.9 on 2022-03-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0031_homeroom_roompart_windowside'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
