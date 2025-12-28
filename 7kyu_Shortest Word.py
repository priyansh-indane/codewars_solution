def find_short(s):
    sp=s.split()
    l=10000000
    for w in sp:
        ln = len(w)
        if ln < l:
            l = ln
    return l
        
