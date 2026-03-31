from itertools import pairwise

def is_monotone(heights):
    
    is_increasing = all(x <= y for x, y in pairwise(heights))
    is_equal = all(x==y for x , y in pairwise(heights))
    is_decreasing=all(x>y for x,y in pairwise(heights))
    
    if is_increasing :
        return True
    
    elif is_equal:
        return True
    
    elif is_decreasing:
        return False
    
    elif heights==1 :
        return True
    
    else:
        return False
