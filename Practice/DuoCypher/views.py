from django.shortcuts import render
from .models.Symbols import Symbols


def index(request):
    return render(request, 'index.html')


def rating(request):
    return render(request, 'rating.html')


def profile(request):
    return render(request, 'profile.html')


def translator(request):
    return render(request, 'translator.html')


def sending(request):
    symbols_count = Symbols.objects.count()
    levels_count = symbols_count // 2
    levels = list(range(1, levels_count + 1))

    context = {
        'levels': levels
    }
    return render(request, 'sending.html', context)


def sending_level(request, level):
    context = {
        'level': level
    }
    return render(request, 'sending_level.html', context)


def receiving(request):
    symbols_count = Symbols.objects.count()
    levels_count = symbols_count // 2
    levels = list(range(1, levels_count + 1))

    context = {
        'levels': levels
    }
    return render(request, 'receiving.html', context)


def receiving_level(request, level):
    context = {
        'level': level
    }
    return render(request, 'receiving_level.html', context)

