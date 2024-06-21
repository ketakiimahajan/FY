
tuplist = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)] #initializing list

k = int(input("enter value of k: ")) # k=2

new_tuplist = []

# filtering tuples not of length k

for tup in tuplist: # iterating through each tuple e.g (4,5), (4,), (8,6,7)...etc 
    if len(tup) != k: # checking if tuple is not equal to k and adding into empty list
        new_tuplist.append(tup) 

print("initial list is: ", str(tuplist))
print("k = ", k)
            
print("tuples in list that are not of length k: " , str(new_tuplist)) 
