# views.py file contains Python functions called "view functions" that handle HTTP requests and return HTTP responses

from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {
            "title": "Sample 1"
        },
        {
            "title": "Sample 2"
        },
        {
            "title": "Sample 3"
        }
    ]
}

def movies(request):
    return render(request, "movies/movies.html", data)