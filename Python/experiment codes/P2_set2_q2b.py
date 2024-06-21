list1 = [1, 6, 7, 10, 13, 32]
list2 = [13, 17, 18, 32]

intersection = list(filter(lambda x: x in list1, list2)) # intersection of two lists
print("intersection of list 1 and list 2 is: ", intersection)

difference1_2 = list(filter(lambda x: x not in list2, list1)) # elements in list1 but not in list2
print("list 1 - list2: ", difference1_2)

difference2_1 = list(filter(lambda x: x not in list1, list2)) # elements in list2 but not in list1
print("list 2 - list 1: ", difference2_1)

union = list(set(list1 + list2)) # union of the two lists
print("union of list1 and list2 is: ", union)