def vowel_indices(word):
    ls=[]
    for i,x in enumerate(word):
        if(x in"AEIOUaeiouyY"):
            ls.append(i+1)
        else:
            pass
            
    return ls     
