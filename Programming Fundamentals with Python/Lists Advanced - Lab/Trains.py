train = [0] * int(input())

command = input()

while command != "End":
    if "add" in command:
        people = int(command.split()[1])
        train[-1] += people
    elif "insert" in command:
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] += people
    elif "leave" in command:
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] -= people

    command = input()

print(train)
