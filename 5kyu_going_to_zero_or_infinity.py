def going(n):
    fact = 1
    s = 0
    result = 0
    for i in range(1, n + 1):
        fact *= i
        s += fact
        result = s / fact
    return result
