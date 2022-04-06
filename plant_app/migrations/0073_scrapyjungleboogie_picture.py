# Generated by Django 3.2.9 on 2022-03-31 19:12

from django.db import migrations
import django_base64field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0072_remove_scrapyjungleboogie_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapyjungleboogie',
            name='picture',
            field=django_base64field.fields.Base64Field(blank=True, default='', max_length=900000, null=True),
        ),
    ]