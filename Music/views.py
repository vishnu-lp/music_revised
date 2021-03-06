# -*- coding: utf-8 -*-


from __future__ import unicode_literals
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Music
from .serializers import MusicSerializer


from rest_framework.generics import (ListAPIView,
	DestroyAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	CreateAPIView)

class MusicListAPI(ListAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer



class MusicDestroyAPI(DestroyAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer



class MusicRetrieveAPI(RetrieveAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer



class MusicCreateAPI(CreateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer



class MusicUpdateAPI(UpdateAPIView):
	queryset = Music.objects.all()
	serializer_class = MusicSerializer



def musicindex(request):
	queryset = Music.objects.all()	
	context = {'queryset':queryset}
	query = request.GET.get("q")
	if query is not None:
		queryset=Music.objects.filter(Q( music_title__icontains = query ) |Q(music_genre__genre_title__contains=query))



	page = request.GET.get('page', 1)
	paginator = Paginator(queryset, 3)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	context = {'queryset':queryset,'users':users}



	return render(request,'music_index.html',context)


