def solve(s):
    count1 = 0
    count2 = 0
    
    for x in s:
        if x.islower():
            count1 += 1
        elif x.isupper():
            count2 += 1
            
    if count1 >= count2:
        return s.lower()
    else:
        return s.upper()
        
