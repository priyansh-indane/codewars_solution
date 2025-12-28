def sum_two_smallest_numbers(numbers):
    
    min1=min(numbers)
        
    numbers.remove(min(numbers))
        
    min2=min(numbers)
        
    return min1+min2    
    
            
