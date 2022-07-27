password = input()
command = input()

while command != "Done":

    new_password = ""

    if command == "TakeOdd":
        for index in range(1, len(password), 2):
            new_password += password[index]
        print(new_password)

    elif "Cut" in command:
        name, index, length = command.split(" ")
        new_password = list(password)
        for _ in range(int(length)):
            new_password.pop(int(index))
        new_password = ''.join(new_password)
        print(new_password)

    else:
        name, substring, substitute = command.split(" ")
        if substring in password:
            new_password = password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

    if new_password:
        password = new_password
    command = input()

print(f'Your password is: {password}')
