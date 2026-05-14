def calculate(num1, operation, num2): 
    
    if operation=='+':
        res=num1+num2
        return res
    
    elif operation=="-":
        res=num1-num2
        return res
    
    elif operation=='*':
        res=num1*num2
        return res
    
    elif operation=='/':
        if num2==0:
            return None
        else :
            return num1/num2
        
    elif num2==0:
        return None
   
