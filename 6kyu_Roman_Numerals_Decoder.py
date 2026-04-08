def solution(roman: str) -> int:
    """complete the solution by transforming the roman numeral into an integer"""
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    prev = 0
    
    for symbol in reversed(roman):
        curr = values[symbol]
        total += curr if curr >= prev else -curr
        prev = curr
    
    return total
