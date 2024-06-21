print("ketaki mahajan / P1-2/ 16014022050")
class InvalidPasswordError(Exception):
    pass

def check_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        raise InvalidPasswordError("Password must contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        raise InvalidPasswordError("Password must contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        raise InvalidPasswordError("Password must contain at least one digit.")

    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    
    if not any(char in special_characters for char in password):
        raise InvalidPasswordError("Password must contain at least one special character.")

    print("Password is valid.")

password = input("Enter a password: ")
try:
    check_password(password)
except InvalidPasswordError as e:
    print("Invalid password:", str(e))