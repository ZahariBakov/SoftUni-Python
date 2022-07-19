phonebook = {}

while True:
    command = input()

    if "-" in command:
        command = command.split("-")
        phonebook[command[0]] = command[1]

    else:
        break

for i in range(int(command)):
    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")

    else:
        print(f"Contact {name} does not exist.")
