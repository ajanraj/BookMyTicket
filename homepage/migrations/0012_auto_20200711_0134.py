# Generated by Django 3.0.8 on 2020-07-10 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0011_auto_20200711_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='movies',
            name='poster_link',
            field=models.CharField(max_length=200),
        ),
    ]
