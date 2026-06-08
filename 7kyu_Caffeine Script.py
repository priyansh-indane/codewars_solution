def caffeine_buzz(n):
    
    if n%3==0 and n%4==0 and n%2==0:
        return "CoffeeScript"
    
    elif n%3==0 and n%4==0:
        return "Coffee"
    
    elif n%3==0 and n%2==0:
        return "JavaScript"
    
    elif n%3==0:
        return "Java"
    
    else:
        return "mocha_missing!"
