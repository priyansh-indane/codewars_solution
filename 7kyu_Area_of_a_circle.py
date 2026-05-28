import math
def circle_area(r):
    if r==0:
        raise ValueError
    
    elif r<=-1:
        raise  ValueError
    
    else:
        return math.pi * r **2
