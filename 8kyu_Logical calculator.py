def logical_calc(array, op):
    
    result = array[0]
    
    for x in array[1:]:
        
        if op == 'AND': result = result and x
        elif op == 'OR': result = result or x
        else: result = result ^ x
        
    return result
