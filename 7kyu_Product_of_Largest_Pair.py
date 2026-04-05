def max_product(a):
    a = a[:]  
    max1 = max(a)
    a.pop(a.index(max1))
    max2 = max(a)
    return max1 * max2
