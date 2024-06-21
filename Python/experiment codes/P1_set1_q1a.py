dec_num = int(input("enter a decimal number: "))

# converting decimal to binary

bin_num = "" # initializing empty string to store the binary number

while dec_num > 0:
    bin_num = str(dec_num % 2) + bin_num # get remainder 0 or 1 and add to empty string 
    dec_num = dec_num // 2 # rounds to whole number 

print(f"conversion of {dec_num} to binary is: {bin_num}")
