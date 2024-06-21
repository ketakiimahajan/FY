print("ketaki mahajan / P1-2 / 16014022050")

class EmptyListError(Exception):
    pass
def calculate_average(numbers):
    if not numbers:
        raise EmptyListError("The list is empty. Cannot calculate average.")
        
    total = sum(numbers)
    average = total / len(numbers)
    
    return average

numbers_list = (input("Enter a list of numbers: ")).split()

try:
    numbers = [float(num) for num in numbers_list]
    average = calculate_average(numbers)
 
    print("Average:", average)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except EmptyListError as e:
    print("Error:", str(e))C
    