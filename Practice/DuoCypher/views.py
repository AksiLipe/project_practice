from django.shortcuts import render
from django.http import JsonResponse
from .models.Symbols import Symbols


def index(request):
    return render(request, 'index.html')


def rating(request):
    return render(request, 'rating.html')


def profile(request):
    return render(request, 'profile.html')


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


def translator(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')
        source_lang = request.POST.get('source_lang', 'en')
        target_lang = request.POST.get('target_lang', 'morse')

        translated_text = ''

        if source_lang == 'en' and target_lang == 'morse':
            for char in input_text.upper():
                if Symbols.objects.filter(symbol=char).exists():
                    translated_text += Symbols.objects.get(symbol=char).answer + ' '
                else:
                    translated_text += '?'
        elif source_lang == 'morse' and target_lang == 'en':
            morse_to_text = {s.answer: s.symbol for s in Symbols.objects.all()}
            for code in input_text.split():
                translated_text += morse_to_text.get(code, '?')

        context = {
            'input_text': input_text,
            'translated_text': translated_text.strip(),
            'source_lang': source_lang,
            'target_lang': target_lang,
        }
        return render(request, 'translator.html', context)

    return render(request, 'translator.html')
