import math
def area(d, l):
    
    if d > l :
        return round(l * math.sqrt(d**2 - l**2), 2)
         
    else:
        return "Not a rectangle"
