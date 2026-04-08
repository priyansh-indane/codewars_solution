def divisors(n):
    divs = [i for i in range(2, n) if n % i == 0]
    return divs if divs else f"{n} is prime"
