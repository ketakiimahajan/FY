employees = [
{"name": "John Doe", "age": 25, "salary": 40000.0},
{"name": "Jane Doe", "age": 35, "salary": 60000.0},
{"name": "Bob Smith", "age": 45, "salary": 80000.0},
{"name": "Alice Johnson", "age": 30, "salary": 55000.0},
{"name": "Mike Williams", "age": 28, "salary": 45000.0},
]

# filtering employees > 30
print("employees above the age of 30: ")
aboveAge = filter(lambda y: y['age'] > 30, employees)
for y in aboveAge:
    print(y)

# increase salary by 10%
print("\nemployees with increased salary")
increSalary = map(lambda y: {'name': y['name'], 'age': y['age'], 'salary': round(y['salary']*1.1)}, employees)
for y in increSalary:
    print(y)

# filtering employees with salary > 50000
print("\nemployees with salary above 50000")
aboveSalary = filter(lambda y: y['salary'] > 50000, employees)
for y in aboveSalary:
    print(y)