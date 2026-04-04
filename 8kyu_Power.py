def number_to_pwr(number, p):
    result = 1
    for _ in range(p):
        result *= number
    return result
