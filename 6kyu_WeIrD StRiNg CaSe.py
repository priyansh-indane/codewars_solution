def to_weird_case(words):
    return ' '.join(
        ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w))
        for w in words.split(' ')
    )
