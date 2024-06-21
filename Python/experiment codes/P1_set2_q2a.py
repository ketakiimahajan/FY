def updated_tuple(tupList, i, k): 
    
    result = [] # initializing list
    
    for tup in tupList: # iterating through each tuple
        tupTolist = list(tup) # converting to list
        tupTolist[i] = k # update values at index i with k
        result.append(tuple(tupTolist)) 
    
    return result

tupList = [(1,3,7),(3,7,5),(7,8,9,0)]
i = int(input("enter i: "))
k = int(input("enter k: "))

result = updated_tuple(tupList, i, k)
print(result)