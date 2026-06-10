def find_digit(num, nth):
    
    if nth <= 0:
        return -1
    
    digits = str(abs(num))
    
    
    if nth > len(digits):
        return 0
    
    return int(digits[-nth])
