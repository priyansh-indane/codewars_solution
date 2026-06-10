import math
def equable_triangle(a,b,c):
    
    s=(a+b+c)/2
    area=s*(s-a)*(s-b)*(s-c)
    square_root=math.sqrt(area)
    
    perimeter=a+b+c
    
    if ( square_root==perimeter):
        return True
    
    else:
        return False
    
