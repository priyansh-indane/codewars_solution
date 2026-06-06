import math
def cooking_time(eggs):
    
    if(eggs==0):
        return 0
    
    elif(eggs<=8):
        return 5
    
    else:
        return math.ceil(eggs/8)*5
    
