# Generated by Django 3.2.9 on 2022-03-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
