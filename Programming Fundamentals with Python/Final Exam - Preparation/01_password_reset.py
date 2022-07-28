password = input()
command = input()

while command != "Done":

    command = command.split(' ')

    if "TakeOdd" == command[0]:
        password = ''.join([password[i] for i in range(1, len(password), 2)])
        print(password)

    elif "Cut" == command[0]:
        index = int(command[1])
        length = int(command[2])
        password = ''.join([password[i] for i in range(len(password)) if i < index or i >= index + length])
        print(password)

    elif "Substitute" == command[0]:
        substring = command[1]
        substitute = command[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()

print(f'Your password is: {password}')
