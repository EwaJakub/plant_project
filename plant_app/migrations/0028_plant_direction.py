# Generated by Django 3.2.9 on 2022-03-17 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0027_auto_20220317_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='direction',
            field=models.IntegerField(choices=[(1, 'okno w kierunku wschodnim'), (2, 'okno w kierunku zachodnim'), (3, 'okno w kierunku północnym'), (4, 'okno w kierunku południowym')], null=True),
        ),
    ]
