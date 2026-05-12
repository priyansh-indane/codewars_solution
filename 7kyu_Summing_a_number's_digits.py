def sum_digits(number):
    
    absolu=abs(number)
    Str=str(absolu)
    add=0
    
    for x in Str:
        add=add+int(x)
        
    return add
