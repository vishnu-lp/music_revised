# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-07 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Genre', '0001_initial'),
        ('Music', '0002_auto_20170427_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='music_genre',
        ),
        migrations.AddField(
            model_name='music',
            name='music_genre',
            field=models.ManyToManyField(to='Genre.Genre'),
        ),
    ]
