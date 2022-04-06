# Generated by Django 3.2.9 on 2022-03-17 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0026_auto_20220316_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='direction',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='room',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='roompart',
        ),
        migrations.CreateModel(
            name='WindowSide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.IntegerField(choices=[(1, 'okno w kierunku wschodnim'), (2, 'okno w kierunku zachodnim'), (3, 'okno w kierunku północnym'), (4, 'okno w kierunku południowym')])),
                ('plants', models.ManyToManyField(related_name='window_sides', to='plant_app.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='RoomPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roompart', models.IntegerField(choices=[(1, 'zacieniony kąt'), (2, 'słoneczny parapet')])),
                ('plants', models.ManyToManyField(related_name='room_part', to='plant_app.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='HomeRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.IntegerField(choices=[(1, 'kuchnia'), (2, 'łazienka'), (3, 'pokój dzienny')])),
                ('plants', models.ManyToManyField(related_name='home_room', to='plant_app.Plant')),
            ],
        ),
    ]
