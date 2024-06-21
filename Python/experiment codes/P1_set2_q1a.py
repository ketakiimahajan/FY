bin_num = input("enter binary number: ")
dec_num = 0 # initializes deciaml num

power = len(bin_num) - 1 # highest power of binary

for num in bin_num: # loops through each num in binary
    dec_num = dec_num + (int(num) * (2 ** power)) # adds powers to decimal
    power = power - 1 # decrements power

print("decimal number is: ", dec_num)
