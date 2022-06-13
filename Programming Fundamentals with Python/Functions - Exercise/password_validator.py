def length_valid(text):
    if 6 <= len(text) <= 10:
        return True
    else:
        print("Password must be between 6 and 10 characters")
        return False


def two_digits(text):
    digit = 0
    for char in text:
        if char.isdigit():
            digit += 1
    if digit >= 2:
        return True
    else:
        print("Password must have at least 2 digits")
        return False


def is_letters_and_digit(text):
    if text.isalnum():
        return True
    else:
        print("Password must consist only of letters and digits")
        return False


password = input()
password_validator = [length_valid(password), two_digits(password), is_letters_and_digit(password)]

if all(password_validator):
    print("Password is valid")


