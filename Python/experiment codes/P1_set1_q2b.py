def center(input_string, width):
    if len(input_string) >= width:
        return input_string
    
    dashes = width - len(input_string) # 10-5=5
    leftDashes = dashes // 2 # 5//2=2
    rightDashes = dashes - leftDashes # 5-2=3
    
    result = ('-' * rightDashes) + input_string + ('-' * leftDashes) # concatenating strings 
    
    return result

input_string = input("enter a string: ") # hello
width = int(input("enter width: ")) # 10

result = center(input_string, width)

print(result)