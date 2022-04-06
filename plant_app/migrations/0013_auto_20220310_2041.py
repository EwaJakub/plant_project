# Generated by Django 3.2.9 on 2022-03-10 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0012_auto_20220309_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='influence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_influence', to='plant_app.animalinfluence'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='purifying',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='air_purifying', to='plant_app.airpurifying'),
        ),
    ]