names_of_gifts = input().split(" ")
command = input()

final_string =""

while command != "No Money":
    command = command.split(" ")
    current_command = command[0]
    current_gift = command[1]
    if current_command == "OutOfStock":
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i] == current_gift:
                names_of_gifts[i] = "None"
    elif current_command == "Required":
        gift_index = int(command[2])
        if gift_index in range(len(names_of_gifts)):
            names_of_gifts[gift_index] = current_gift
    else:
        names_of_gifts.pop()
        names_of_gifts.append(current_gift)
    command = input()

for string in names_of_gifts:
    if string != "None":
        final_string += string + " "

print(final_string)


