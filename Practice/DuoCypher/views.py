from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models.Symbols import Symbols
from django.contrib import messages


def base(request):
    return render(request, 'base.html')


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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(base)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(base)  # Перенаправьте на домашнюю страницу
        else:
            messages.error(request, "Ошибка авторизации. Проверьте введенные данные.")
    else:
        form = AuthenticationForm()
    return render(request, 'login_view.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect(base)
