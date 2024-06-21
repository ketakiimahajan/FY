import re

def is_valid(ip_address):

    pattern = r'^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]\.){3}[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]$'
    # num from 0-9, 10-99, 100-199, 200-249, 250-255) and . repeats 3 times, same pattern without . for last num
    
    if re.match(pattern, ip_address): # using re.match to match input with pattern
        return True
    else:
        return False

print("121.18.19.20 is:", is_valid('121.18.19.20')) # true
print("321.18.19.20 is:", is_valid('321.18.19.20')) # false
print("120.34..45 is:", is_valid('120.34..45')) # false
print("0.1.2.3 is:", is_valid('0.1.2.3 is')) # true
