# Generated by Django 3.0.8 on 2020-07-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20200711_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster_link',
            field=models.CharField(default='Image', max_length=1000),
        ),
    ]
