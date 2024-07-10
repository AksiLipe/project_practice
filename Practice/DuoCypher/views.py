import json
from django.http import JsonResponse
from .forms import AnswerForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models.Symbols import Symbols
from utils.helpers import generate_levels
from utils.helpers import levels_count
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def base(request):
    return render(request, 'base.html')


def profile(request):
    return render(request, 'profile.html')


def sending(request):
    levels = list(range(1, levels_count() + 1))

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
    levels = list(range(1, levels_count() + 1))

    context = {
        'levels': levels
    }
    return render(request, 'receiving.html', context)


def receiving_level(request, level):
    symbols = generate_levels(level)
    form = AnswerForm()
    message = ""
    message_type = ""
    show_next_level = False

    current_symbol_index = request.session.get(f'current_symbol_index_level_{level}', 0)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer'].strip()
            correct_answer = symbols[current_symbol_index].symbol.strip()
            if user_answer.lower() == correct_answer.lower():
                current_symbol_index += 1
                if current_symbol_index == len(symbols):
                    message = "Congratulations! You completed the level."
                    message_type = "success"
                    current_symbol_index = 0
                    if level < levels_count():
                        show_next_level = True
                else:
                    message = 'Correct!'
                    message_type = 'success'
            else:
                message = 'Incorrect. Try again.'
                message_type = 'danger'
        else:
            message = 'Please enter a valid answer.'
            message_type = 'danger'

        request.session[f'current_symbol_index_level_{level}'] = current_symbol_index

    current_symbol = symbols[current_symbol_index]

    context = {
        'level': level,
        'symbols': symbols,
        'current_symbol': current_symbol,
        'form': form,
        'message': message,
        'message_type': message_type,
        'show_next_level': show_next_level
    }

    return render(request, 'receiving_level.html', context)


def translator(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        input_text = data.get('input_text', '')
        source_lang = data.get('source_lang', 'en')
        target_lang = data.get('target_lang', 'morse')

        translated_text = ''

        if source_lang == 'en' and target_lang == 'morse':
            for char in input_text.upper():
                if Symbols.objects.filter(symbol=char).exists():
                    translated_text += Symbols.objects.get(symbol=char).answer + ' '
                else:
                    translated_text += '? '
        elif source_lang == 'morse' and target_lang == 'en':
            morse_to_text = {s.answer: s.symbol for s in Symbols.objects.all()}
            for code in input_text.split():
                translated_text += morse_to_text.get(code, '?')

        response_data = {
            'input_text': input_text,
            'translated_text': translated_text.strip(),
            'source_lang': source_lang,
            'target_lang': target_lang,
        }
        return JsonResponse(response_data)

    return render(request, 'translator.html')


def reset_level(request, level):
    request.session[f'current_symbol_index_level_{level}'] = 0

    return redirect('receiving_level', level=level)


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
