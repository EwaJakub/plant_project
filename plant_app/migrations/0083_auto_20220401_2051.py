# Generated by Django 3.2.9 on 2022-04-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0082_alter_scrapyjungleboogie_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapyjungleboogie',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='scrapyzielonyparapet',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
