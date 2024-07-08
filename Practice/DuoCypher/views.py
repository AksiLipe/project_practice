from django.shortcuts import render, redirect
from .forms import AnswerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models.Symbols import Symbols
from utils.helpers import generate_levels
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.shortcuts import render, redirect
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
    symbols_count = Symbols.objects.exclude(answer='  ').count()
    levels_count = symbols_count // 2
    levels = list(range(1, levels_count + 1))

    context = {
        'levels': levels
    }
    return render(request, 'sending.html', context)


def sending_level(request, level):
    context = {
        'level': level,
        'symbols': generate_levels(level)
    }
    return render(request, 'sending_level.html', context)


def receiving(request):
    symbols_count = Symbols.objects.exclude(answer='  ').count()
    levels_count = symbols_count // 2
    levels = list(range(1, levels_count + 1))

    context = {
        'levels': levels
    }
    return render(request, 'receiving.html', context)


def receiving_level(request, level):
    symbols = generate_levels(level)
    form = AnswerForm()
    message = ""
    message_type = ""

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer'].strip()
            correct_answer = get_correct_answer(level).strip()
            if user_answer.lower() == correct_answer.lower():
                message = 'Correct!'
                message_type = 'success'
            else:
                message = 'Incorrect. Try again.'
                message_type = 'danger'
        else:
            message = 'Please enter a valid answer.'
            message_type = 'danger'

    context = {
        'level': level,
        'symbols': symbols,
        'form': form,
        'message': message,
        'message_type': message_type
    }

    return render(request, 'receiving_level.html', context)


def get_correct_answer(level):
    symbols_for_level = generate_levels(level)
    correct_answer = symbols_for_level[0].symbol
    return correct_answer

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
