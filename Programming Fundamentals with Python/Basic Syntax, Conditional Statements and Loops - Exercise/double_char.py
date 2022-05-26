command = input()

while command != "End":
    new_string = ""
    if command == "SoftUni":
        command = input()
        continue
    for char in command:
        new_string += char + char
    print(new_string)
    command = input()
