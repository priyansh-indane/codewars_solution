def next_letter(s):
    result = ''
    
    for x in s:
        if x.isalpha():
            if x == 'z':
                result += 'a'
            elif x == 'Z':
                result += 'A'
            else:
                result += chr(ord(x) + 1)
        else:
            result += x
            
    return result
