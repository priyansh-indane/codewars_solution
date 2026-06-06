def arrange(arr):
    
    def convert_gram(s):
        if s.endswith('KG'):
            return float(s[:-2])*1000
        
        elif s.endswith('T'):
            return float(s[:-1])*1000000
        
        else:
            return float(s[:-1])
            
    return sorted(arr,key=convert_gram)
    
