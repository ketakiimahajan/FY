import re

print("ketaki mahajan / P1-2 / 16014022050")

str = input("enter a string: ")

pattern = r'[^A-Za-z0-9]+' #matches characters that are not A-Z, a-z, 0-9

new_str = re.sub(pattern, '', str) #searches for non-alphanumeric characters and replaces with empty string

print("string without aplha-numeric characters: ", new_str) # prints new string 