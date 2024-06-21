def write_employee_details(file_name):
    with open(file_name, "w") as file:
        file.write("EmpId\tName\t\tDepartment\n")
        
        while True:
            emp_id = input("Enter Employee ID (or 'q' to quit): ")
            if emp_id == "q":
                break
            
            name = input("Enter Employee Name: ")
            department = input("Enter Employee Department: ")
            
            line = f"{emp_id}\t{name}\t\t{department}\n"
            file.write(line)
            
        print("Employee details have been saved to employeedetails.txt.")

file_name = "employeedetails.txt"
write_employee_details(file_name)
