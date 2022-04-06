# Generated by Django 3.2.9 on 2022-03-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0060_scrapyzielonyparapet'),
    ]

    operations = [
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
                'verbose_name': 'Scrapped zielonyparapet plants',
            },
        ),
    ]
