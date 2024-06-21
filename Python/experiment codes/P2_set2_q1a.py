print("ketaki mahajan / P1-2 / 16014022050")
numbers = input("enter numbers: ").split() # input list (as string)
numbers = list(map(int, numbers)) # converts string list to int list 

positive = 0
negative = 0
zero = 0

for num in numbers: # iterates through each number in list to check whether positive/negative/zero
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("positive: ", positive)
print("negative: ", negative)
print("zero: ", zero)