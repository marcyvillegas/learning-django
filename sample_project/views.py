# views.py file contains Python functions called "view functions" that handle HTTP requests and return HTTP responses

from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def movies(request):
    data = Movie.objects.all()
    return render(request, "movies/movies.html", {'movies': data})

def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, "movies/detail.html", {'movie': data})