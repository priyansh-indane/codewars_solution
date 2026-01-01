def max_tri_sum(numbers):
    s=list(set(numbers))
    ###return sum(sorted(set(numbers), reverse=True)[:3])
    

    max1=0
    max2=0
    max3=0
    if(len(s)==3 or len(s)>3):
        max1=max(s)
        s.remove(max1)
        max2=max(s)
        s.remove(max2)
        max3=max(s)
    else:
        pass
    
    return max1+max2+max3
    
