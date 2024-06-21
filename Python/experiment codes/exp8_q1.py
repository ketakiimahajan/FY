print("ketaki mahajan / P1-2 / 16014022050")
def get_name():
    while True:
        name = input("enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid input! Please enter a valid name.")

def get_surname():
    while True:
        surname = input("enter your surname: ")
        if surname.isalpha():
            return surname
        else:
            print("Invalid input! Please enter a valid surname.")

def get_age():
    while True:
        age = input("enter your age: ")
        if age.isdigit():
            return int(age)
        else:
            print("Invalid input! Please enter a valid age.")

def get_height():
    while True:
        height = input("Enter your height (in meters): ")
        try:
            height = float(height)
            return height
        except ValueError:
            print("Invalid input! Please enter a valid height.")

def get_weight():
    while True:
        weight = input("Enter your weight (in kilograms): ")
        try:
            weight = float(weight)
            return weight
        except ValueError:
            print("Invalid input! Please enter a valid weight.")

name = get_name()
lastName = get_surname()
age = get_age()
height = get_height()
weight = get_weight()

print("\nPersonal Details:")

print("Name: ", name)
print("Last Name: ", lastName)
print("Age: ", age)
print("Height: ", height)
print("Weight: ", weight)