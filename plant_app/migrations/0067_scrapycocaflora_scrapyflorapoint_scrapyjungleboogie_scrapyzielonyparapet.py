# Generated by Django 3.2.9 on 2022-03-31 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0066_auto_20220331_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapyCocaflora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('link', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('picture', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Scrapped cocaflora plants',
            },
        ),
        migrations.CreateModel(
            name='ScrapyFloraPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('link', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('picture', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Scrapped florapoint plants',
            },
        ),
        migrations.CreateModel(
            name='ScrapyJungleBoogie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('link', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('picture', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Scrapped jungleboogie plants',
            },
        ),
        migrations.CreateModel(
            name='ScrapyZielonyParapet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('link', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('picture', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Scrapped zielonyparapet plants',
            },
        ),
    ]
