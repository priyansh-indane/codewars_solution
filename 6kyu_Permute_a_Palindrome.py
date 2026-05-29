def permute_a_palindrome(input):
    counts = {}
    for char in input:
        counts[char] = counts.get(char, 0) + 1
    
    odd_counts = sum(1 for c in counts.values() if c % 2 != 0)
    return odd_counts <= 1
            
    
