import string 

def count_letters_and_digits(s):
    count=0
    ascii_values=string.ascii_letters
    for x in s:
        if(x in ascii_values or x.isdigit()):
            count=count+1
        else:pass    
    return count        
    
