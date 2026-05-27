from math import prod

def process_data(data):
    return prod(a - b for a, b in data)
            
