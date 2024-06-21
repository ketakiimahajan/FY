guest = int(input("enter number of guests: ")) 

total_cost = 0 #initializing total cost

for i in range(guest): #loops through each guest
    age = int(input("Visitor {} age: ".format(i+1)))
    
    if age <= 2: #finding cost based on age
        cost = 0
    
    elif age <= 12:
        cost = 14
    
    elif age >= 65:
        cost = 18
    
    else:
        cost = 23
    total_cost += cost

print("The total admission cost is ${:.2f}.".format(total_cost)) #displaying total cost for group