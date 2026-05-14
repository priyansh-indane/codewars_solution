def capitals(word):
    ls=[]
    for i, x in enumerate(word):
        if x.isupper():
            ls.append(i)
            
    return ls        
            
            
