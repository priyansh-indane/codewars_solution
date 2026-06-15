def largest(n, xs):
    
    ls=[]
    
    for x in range(n):
        
        max_ele=max(xs)
        
        ls.append(max_ele)
        
        xs.remove(max_ele)
        
    return sorted(ls)
        
        
