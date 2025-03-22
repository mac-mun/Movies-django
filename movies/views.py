from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {"id": 5, "title": "Billions", "year": 2015},
        {"id": 6, "title": "Industry", "year": 2019},
        {"id": 7, "title": "Devils", "year": 2022},
    ]
}


def movies(request):
    return render(request, "movies/movies.html", data)


def home(request):
    return HttpResponse("Home Page")
