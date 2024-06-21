def check_divide(number):
    
    # converts number to string to get individual digits
    number_str = str(number)
    
    # loops through each digit of the number
    for digit in number_str:
        if (int(digit) != 0) and (number % int(digit) == 0): # converts digit integer and checks if divisible by original number
            continue
        else:
            return "No"
    
    return "Yes"

number = int(input("enter a number: "))
print(check_divide(number))