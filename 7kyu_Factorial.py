import math
def factorial(n):
    if(n<12):
        result=math.factorial(n)
        return result
    
    elif(n==12):
        return 479001600
    
    elif(n<0):
        return -1
    
    elif(n>12):
        raise ValueError
    
    else:
        return -1
