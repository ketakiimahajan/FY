print("ketaki mahajan / P1-2 / 16014022050")

string = ("The quick brown fox jumps over the laze dog in an ice.")
new_string = string.replace(".", "") # ignorning . as last characters of word becomes . and not considered as vowel

print(string)

words = new_string.split() # split the string into a list of words

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
res = []


for word in words: # iterate each letter in the list
    if len(word) in [3, 4] and (word[-1] in vowels): # checks if word is 3/4 characters long and ends with a vowel

        res.append(word)

print(res)
