# Generated by Django 5.1.2 on 2024-11-03 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videogamemodel',
            options={'verbose_name': 'VideoGame', 'verbose_name_plural': 'VideoGames'},
        ),
        migrations.AlterModelTable(
            name='videogamemodel',
            table='VideoGames',
        ),
    ]
