def sum_array(arr):
    if not arr or (len(arr) in [0, 1]):
        return 0
        
    MAX=0
    MIN=0
    sum=0
    
    MAX=max(arr)
    MIN=min(arr)
    
    arr.remove(MAX)
    arr.remove(MIN)
    
    for x in arr:
        sum=sum+x
        
    return sum  
