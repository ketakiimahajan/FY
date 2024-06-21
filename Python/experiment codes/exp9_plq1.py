def write_file(file_name):
    with open(file_name, "w") as file:
        while True:
            line = input("Enter a line (or 'q' to quit): ")
            if line == "q":
                break
            file.write(line + "\n")

    print("File created successfully.")

def capitalize_file(file_name):
    try:
        with open(file_name, "r+") as file:
            content = file.read()
            file.seek(0)
            file.write(content.upper())
            file.truncate()
        print("File capitalized successfully.")
    except FileNotFoundError:
        print("File not found.")

file_name = input("Enter the file name: ")
write_file(file_name)
capitalize_file(file_name)
