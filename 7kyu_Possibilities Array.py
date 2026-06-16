def is_all_possibilities(arr):
    
    ls=[]
    a=len(arr)
    
    for x in range(0,a):
        ls.append(x)
        
    if sorted(arr) == ls:
        return True
    
    else:
        return False
    
