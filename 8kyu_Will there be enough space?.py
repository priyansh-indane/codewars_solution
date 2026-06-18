def enough(cap, on, wait):
  
    addition=on+wait
    if (addition<=cap):
        return 0
    else:
        return addition-cap
    
