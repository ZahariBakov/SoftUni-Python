message = input()

while True:
    command = input()

    if command == "Decode":
        break

    command = command.split("|")

    if command[0] == "Move":
        index = int(command[1])

        substring = message[index:] + message[:index]
        message = substring

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        substring = ''

        if index < len(message):
            for i, char in enumerate(message):
                if i == index:
                    message = message[:i] + value + message[i:]

        else:
            message += value

    elif command[0] == "ChangeAll":
        old_char = command[1]
        new_char = command[2]

        message = message.replace(old_char, new_char)

print(f"The decrypted message is: {message}")
