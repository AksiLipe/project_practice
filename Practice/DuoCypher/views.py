from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def rating(request):
    return render(request, 'rating.html')


def about(request):
    return render(request, 'about.html')
