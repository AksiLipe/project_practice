from django.shortcuts import render, redirect
from .forms import AnswerForm
from .models.Symbols import Symbols
from utils.helpers import generate_levels


def index(request):
    return render(request, 'index.html')


def rating(request):
    return render(request, 'rating.html')


def profile(request):
    return render(request, 'profile.html')


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
