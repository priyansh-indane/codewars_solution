def correct_polish_letters(st):
    replace = {
        'ą': 'a', 'ć': 'c', 'ę': 'e',
        'ł': 'l', 'ń': 'n', 'ó': 'o',
        'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    
    return ''.join(replace.get(x, x) for x in st)
