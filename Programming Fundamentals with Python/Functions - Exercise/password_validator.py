password = input()


def password_validator(text):
    valid_password = True
    digit = 0
    letters_in_password = 0

    if len(text) < 6 or 10 < len(text):
        valid_password = False
        print("Password must be between 6 and 10 characters")

    for char in text:
        if char.isdigit():
            digit += 1
        else:
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                letters_in_password += 1

    if letters_in_password + digit != len(text):
        valid_password = False
        print("Password must consist only of letters and digits")
    if digit < 2:
        valid_password = False
        print("Password must have at least 2 digits")

    if valid_password:
        print("Password is valid")


password_validator(password)
