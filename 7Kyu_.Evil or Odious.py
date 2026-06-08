def evil(n):
  
    binary=bin(n)
  
    countt=binary.count('1')
  
    if countt%2==0:
        return "It's Evil!"
    else :
        return "It's Odious!"
