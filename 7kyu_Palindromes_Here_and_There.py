def is_palindrome(n):
    n = str(n)
    reverse_n = n[::-1]
    if(reverse_n == n):
        return True
    else:
        return False

def convert_palindromes(numbers):
    arr = []
    
    for x in numbers:
        if(is_palindrome(x)):
            arr.append(1)
        else:
            arr.append(0)
            
    return arr
