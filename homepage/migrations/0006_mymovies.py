# Generated by Django 3.0.8 on 2020-07-10 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0005_auto_20200710_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mymovies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.CharField(max_length=20)),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
