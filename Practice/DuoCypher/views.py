from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def rating(request):
    return render(request, 'rating.html')


def about(request):
    return render(request, 'about.html')


def sending(request):
    return render(request, 'sending.html')

def receiving(request):
    return render(request, 'receiving.html')
