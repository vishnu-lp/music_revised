# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import Genre
from .serializers import GenreSerializer

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from rest_framework.generics import (ListAPIView,
	DestroyAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	CreateAPIView)

class GenreListAPI(ListAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer



class GenreDestroyAPI(DestroyAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer



class GenreRetrieveAPI(RetrieveAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer



class GenreCreateAPI(CreateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer



class GenreUpdateAPI(UpdateAPIView):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer


def Genreindex(request):

	queryset = Genre.objects.all()	
	context = {'queryset':queryset}
	paginator = Paginator(queryset, 8)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	context = {'queryset':queryset,'contacts':contacts}

	return render(request,'base.html',context)