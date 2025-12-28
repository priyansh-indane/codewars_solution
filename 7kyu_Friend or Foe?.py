def check(x):
    a=len(x)
    
    if(a==4):
        return True
    
    else:
        return False
        
def friend(x):
    
    output=list(filter(check,x))
    return output
