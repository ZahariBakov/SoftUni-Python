def contains(text, string):
    if string in text:
        print(f"{text} contains {string}")

    else:
        print("Substring not found!")


def flip(text, command, start, end):
    list_of_text = []
    for char in text:
        list_of_text.append(char)

    if command == "Upper":
        for i in range(len(text)):
            if start <= i < end:
                list_of_text[i] = list_of_text[i].upper()

    else:
        for i in range(len(text)):
            if start <= i < end:
                list_of_text[i] = list_of_text[i].lower()

    text = ''.join(list_of_text)
    print(text)

    return text


def slice(text, start, end):
    text = ''.join([text[i] for i in range(len(text)) if i < start or i >= end])
    print(text)

    return text


activation_key = input()

while True:
    command = input()

    if command == "Generate":
        break

    command = command.split(">>>")

    if command[0] == "Contains":
        substring = command[1]
        contains(activation_key, substring)

    elif command[0] == "Flip":
        second_command = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        activation_key = flip(activation_key, second_command, start_index, end_index)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = slice(activation_key, start_index, end_index)

print(f"Your activation key is: {activation_key}")
