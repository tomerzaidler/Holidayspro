# Generated by Django 2.2.6 on 2019-10-09 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodayHolidays', '0002_song_song_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
