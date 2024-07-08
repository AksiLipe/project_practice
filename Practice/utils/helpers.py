from DuoCypher.models.Symbols import Symbols


def generate_levels(level):
    symbols_all = list(Symbols.objects.all().exclude(answer='  '))
    symbols_all.sort(key=lambda x: len(x.answer))

    n = level
    symbols_count = n * 2
    symbols = symbols_all[:symbols_count]
    repeat = symbols[:symbols_count-2]
    curr_level = symbols[symbols_count-2:]
    repeat.sort(key=lambda x: len(x.answer))
    result = curr_level + repeat

    return result
