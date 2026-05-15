def fix_parentheses(s):
    o = c = 0
    for ch in s:
        if ch == '(': c += 1
        elif c: c -= 1
        else: o += 1
    return '(' * o + s + ')' * c
