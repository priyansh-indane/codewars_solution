def get_middle(s):
    if(len(s)%2==0):
        L=len(s)
        st=(L//2)-1
        end=st+2
        
        return s[st:end]
    
    else:
        L=len(s)
        S=(L//2)
        return s[S]
