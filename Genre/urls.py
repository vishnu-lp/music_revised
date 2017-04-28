"""Voris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import (GenreListAPI,
	GenreUpdateAPI,
	GenreDestroyAPI,
	GenreCreateAPI,
	GenreRetrieveAPI,Genreindex)

urlpatterns = [
    url(r'^list/$',GenreListAPI.as_view(),name='genre_list'),
    url(r'^update/(?P<pk>\d+)/$',GenreUpdateAPI.as_view(),name='Genre_Update'),
    url(r'^create/$',GenreCreateAPI.as_view(),name='Genre_Create'),
    url(r'^retrieve/(?P<pk>\d+)/$',GenreRetrieveAPI.as_view(),name='Genre_Retrieve'),
    url(r'^destroy/(?P<pk>\d+)/$',GenreDestroyAPI.as_view(),name='Genre_Destroy'),
    url(r'^$',Genreindex,name='genre')


]
