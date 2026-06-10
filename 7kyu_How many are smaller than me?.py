def smaller(arr):
    
    final_arr=[]
    
    for i in range(len(arr)):
        count=0
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                count=count+1
                
        final_arr.append(count)
    return final_arr            
        
    
