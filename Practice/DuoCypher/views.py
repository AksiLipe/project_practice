from django.shortcuts import render
from .models.Symbols import Symbols


def index(request):
    return render(request, 'index.html')


def rating(request):
    return render(request, 'rating.html')


def about(request):
    return render(request, 'about.html')


def sending(request):
    symbols_count = Symbols.objects.count()
    levels_count = symbols_count // 2
    levels = list(range(1, levels_count + 1))

    context = {
        'levels': levels
    }
    return render(request, 'sending.html', context)


def receiving(request):
    return render(request, 'receiving.html')

