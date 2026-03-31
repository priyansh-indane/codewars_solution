def positive_sum(arr):
    sum=0
    for x in arr:
        if x > 0:
            sum=sum+x
        
        elif x<0:
            pass
        
        else:
            return 0
        
    return sum    
        
