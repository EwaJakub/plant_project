# Generated by Django 3.2.9 on 2022-03-23 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0038_delete_plantwebuser'),
        ('home_app', '0012_auto_20220323_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='plants',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='plants',
            field=models.ManyToManyField(null=True, related_name='my_plants_profile', to='plant_app.Plant'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='wishlist',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='wishlist',
            field=models.ManyToManyField(null=True, related_name='wish_list_profile', to='plant_app.Plant'),
        ),
    ]
