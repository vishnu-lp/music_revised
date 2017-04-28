from django.conf.urls import url
from django.contrib import admin
from .views import (MusicListAPI,
	MusicUpdateAPI,
	MusicDestroyAPI,
	MusicCreateAPI,
	MusicRetrieveAPI)

urlpatterns = [
    url(r'^$',MusicListAPI.as_view(),name='Music_list'),
    url(r'^update/(?P<pk>\d+)/$',MusicUpdateAPI.as_view(),name='Music_Update'),
    url(r'^create/$',MusicCreateAPI.as_view(),name='Music_Create'),
    url(r'^retrieve/(?P<pk>\d+)/$',MusicRetrieveAPI.as_view(),name='Music_Retrieve'),
    url(r'^destroy/(?P<pk>\d+)/$',MusicDestroyAPI.as_view(),name='Music_Destroy')
 

]
