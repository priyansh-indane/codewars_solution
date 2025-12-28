def get_count(sentence):
    count=0
    for w in sentence:
        if(w=='a' or w=='e' or w=='i' or w=='o' or w=='u'):
            count=count+1
            
    return count 
