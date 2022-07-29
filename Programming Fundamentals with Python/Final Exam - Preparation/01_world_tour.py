def add_stop(text, index, string):
    new_text = ''
    if 0 <= index < len(text):
        for i in range(len(text)):
            if i == index:
                new_text += string
            new_text += text[i]
        text = new_text
        print(text)

    return text


def remove_stop(text, start, end):
    if 0 <= start < len(text) and 0 <= end < len(text):
        text = ''.join([text[i] for i in range(len(text)) if i < start or i > end])
    print(text)

    return text


def switch(text, old, new):
    if old in text:
        text = text.replace(old, new)
        print(text)

    return text


travel = input()

while True:
    command = input()

    if command == "Travel":
        break

    command = command.split(":")

    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        travel = add_stop(travel, index, string)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        travel = remove_stop(travel, start_index, end_index)

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        travel = switch(travel, old_string, new_string)

print(f"Ready for world tour! Planned stops: {travel}")
