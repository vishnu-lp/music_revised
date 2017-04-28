# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Genre.models import Genre

# Create your models here.


class Music(models.Model):
	music_title = models.CharField(max_length=100,db_index=True)
	music_genre = models.ForeignKey(Genre)
	music_description = models.TextField(max_length=200,blank=True)

	def __str__(self):
		return self.music_title
