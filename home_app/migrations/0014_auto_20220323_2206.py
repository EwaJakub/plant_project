# Generated by Django 3.2.9 on 2022-03-23 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0038_delete_plantwebuser'),
        ('home_app', '0013_auto_20220323_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='plants',
            field=models.ManyToManyField(related_name='my_plants_profile', to='plant_app.Plant'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(related_name='wish_list_profile', to='plant_app.Plant'),
        ),
    ]
