def zero_fuel(distance_to_pump, mpg, fuel_left):
    
    fuel=mpg*fuel_left
    
    if fuel>=distance_to_pump:
        return True
    else:
        return False
    
    
    
