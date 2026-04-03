def hamming_weight(x):
    x_bin = bin(x)
    count = 0
    
    for bit in x_bin:
        if bit == '1':
            count += 1
    
    return count
