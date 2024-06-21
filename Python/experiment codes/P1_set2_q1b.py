import re

def is_valid(date):
    
    pattern = r'^([1-9]|[1-3][0-1])/([1-9]|[1-1][0-2])/([0-9]{4})$'
    # str day from 1-31, slash, month 1-12, slash, 4-digit year
    
    if re.match(pattern, date): # using re.match to match input with pattern
        return True
    else:
        return False
    
print("16/08/2023 is: ", is_valid('16/08/2023')) # T
print("04-26-23 is: ", is_valid('04-26-23')) # F
print("11/11/2000 is: ", is_valid('11/11/2000')) # T
print("08/31/1990 is: ", is_valid('08/31/1990')) # T