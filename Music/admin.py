# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Music
from Genre.models import Genre



class MusicAdmin(admin.ModelAdmin):
	list_display = ['music_title','music_genre','music_description']
	search_fields = ['music_title','music_description','music_genre__genre_title']

admin.site.register(Music,MusicAdmin)