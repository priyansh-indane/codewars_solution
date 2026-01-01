def largest_pair_sum(numbers): 
    max1=0
    max2=0
    
    max1=max(numbers)
    numbers.remove(max1)
    max2=max(numbers)
    
    return max1+max2
   
