import os

while True:
    line = input()

    if line == "End":
        break

    command_parts = line.split("-")
    command, file_name = command_parts[0], command_parts[1]

    if command == "Create":
        with open(f'./{file_name}', 'w') as file:
            pass

    elif command == "Add":
        text = command_parts[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(f"{text}\n")

    elif command == "Replace":
        old_string, new_string = command_parts[2], command_parts[3]

        try:
            with open(f'./{file_name}', 'r') as file:
                text = file.read().replace(old_string, new_string)
            with open(f'./{file_name}', 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")

    else:
        try:
            os.remove(f'./{file_name}')
        except FileNotFoundError:
            print("An error occurred")
