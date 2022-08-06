def insert_space(text, idx):
    text = text[:idx] + " " + text[idx:]
    print(text)

    return text


def reverse(text, string):
    if string in text:
        text = text.replace(string, '', 1)
        text += string[::-1]
        print(text)

    else:
        print("error")

    return text


def change_all(text, old, new):
    text = text.replace(old, new)
    print(text)

    return text


message = input()

while True:
    command = input()

    if command == "Reveal":
        break

    command = command.split(":|:")

    if "InsertSpace" in command:
        index = int(command[1])
        message = insert_space(message, index)

    elif "Reverse" in command:
        substring = command[1]
        message = reverse(message, substring)

    elif "ChangeAll" in command:
        substring = command[1]
        replacement = command[2]
        message = change_all(message, substring, replacement)

print(f"You have a new text message: {message}")
