
tuplist = [(6,24),(60,12), (18,21)] #initializing list

k = int(input("enter value of k: ")) # k=6

selected_tuplist = []

# filtering tuples with values divisible by k

for tup in tuplist: # iterating through each tuple e.g (6,24), (60,12) etc..
    count = 0
    
    for element in tup: # iterating through each element in tuple e.g 6, 24 etc..
        if (element % k == 0):
            count += 1 # increment count if element is divisible by k  
    
    if count == len(tup): # if count equal length of tuple, it means all elements divisible by k
        selected_tuplist.append(tup) # appending divisible tuple to emply list

print("initial list is: ", str(tuplist))
print("k = ", k)
            
print("tuples in list where all elements divisible by k : " , str(selected_tuplist)) # printing tuple list with all elements divisible by k
