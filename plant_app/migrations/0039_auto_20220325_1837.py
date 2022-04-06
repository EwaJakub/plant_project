# Generated by Django 3.2.9 on 2022-03-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_app', '0038_delete_plantwebuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapyJungleBoogie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('link', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name': 'Scrapped plants',
            },
        ),
        migrations.DeleteModel(
            name='ScrapyItem',
        ),
    ]
