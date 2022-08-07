def make_upper(text, idx):
    substring = ''
    for i in range(len(text)):
        if i == idx:
            substring += text[i].upper()
        else:
            substring += text[i]

    text = substring
    print(text)

    return text


def make_lower(text, idx):
    substring = ''
    for i in range(len(text)):
        if i == idx:
            substring += text[i].lower()
        else:
            substring += text[i]

    text = substring
    print(text)

    return text


def insert(text, idx, letter):
    substring = ''
    if 0 <= idx < len(text):
        for i in range(len(text)):
            if i == idx:
                substring += letter
            substring += text[i]

        text = substring

    print(text)

    return text


def replace(text, letter, num):
    if letter in text:
        new_letter = ord(letter) + num
        new_letter = chr(new_letter)
        text = text.replace(letter, new_letter)

    print(text)

    return text


def validation(text):
    if len(text) < 8:
        print("Password must be at least 8 characters long!")

    substring = ''
    upper_char = False
    lower_char = False
    digit_char = False

    for char in text:
        if ord(char) == 33 or ord(char) == 95 or char.isalnum():
            substring += char

        if char.isupper():
            upper_char = True

        if char.islower():
            lower_char = True

        if char.isdigit():
            digit_char = True

    if substring != text:
        print("Password must consist only of letters, digits and _!")

    if not upper_char:
        print("Password must consist at least one uppercase letter!")

    if not lower_char:
        print("Password must consist at least one lowercase letter!")

    if not digit_char:
        print("Password must consist at least one digit!")

    return text


password = input()

while True:
    command = input()

    if command == "Complete":
        break

    command = command.split(" ")

    if "Upper" in command:
        index = int(command[2])
        password = make_upper(password, index)

    elif "Lower" in command:
        index = int(command[2])
        password = make_lower(password, index)

    elif "Insert" in command:
        index = int(command[1])
        char = command[2]
        password = insert(password, index, char)

    elif "Replace" in command:
        char = command[1]
        value = int(command[2])
        password = replace(password, char, value)

    elif "Validation" in command:
        password = validation(password)
