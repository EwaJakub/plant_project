# Generated by Django 3.2.9 on 2022-03-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0064_scrapycocaflora'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scrapycocaflora',
            options={'verbose_name': 'Scrapped cocaflora plants'},
        ),
        migrations.AlterModelOptions(
            name='scrapyflorapoint',
            options={'verbose_name': 'Scrapped florapoint plants'},
        ),
        migrations.AddField(
            model_name='plant',
            name='search_key',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
