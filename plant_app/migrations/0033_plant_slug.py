# Generated by Django 3.2.9 on 2022-03-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0032_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
