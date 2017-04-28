# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Genre(models.Model):
	genre_title = models.CharField(max_length=200,db_index=True)
	desc = models.TextField(max_length=200,db_index=True)


	def __str__(self):
		return self.genre_title
