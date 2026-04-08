from collections import deque

def sequence_gen(*args):
    window = deque(args)
    x = len(args)
    
    for term in args:
        yield term
    
    while True:
        next_term = sum(window)
        window.append(next_term)
        window.popleft()
        yield next_term
