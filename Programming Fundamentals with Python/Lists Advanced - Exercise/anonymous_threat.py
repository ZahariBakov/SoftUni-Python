strings = input().split()
command = input()

while command != "3:1":
    if "merge" in command:
        start_index = int(command.split()[1])
        end_index = int(command.split()[2])
        temporary_list = []
        for i in range(start_index, end_index + 1):
            if len(strings) > start_index:
                temporary_list.append(strings.pop(start_index))
        temporary_string = "".join(temporary_list)
        strings.insert(start_index, temporary_string)
    elif "divide" in command:
        index = int(command.split()[1])
        divider = int(command.split()[2])
        temporary_string = list(strings.pop(index))
        length = len(temporary_string) // divider
        temporary_list = []
        adding_characters = ""
        length_temporary = len(temporary_string)
        for i in range(length_temporary):
            adding_characters += temporary_string.pop(0)
            if len(adding_characters) == length:
                temporary_list.append(adding_characters)
                adding_characters = ""
                if len(temporary_list) == divider:
                    break
        if temporary_string != []:
            adding_characters = temporary_list.pop()
            for i in temporary_string:
                adding_characters += temporary_string.pop(0)
            temporary_list.append(adding_characters)
        if temporary_list != []:
            for i in range(divider):
                strings.insert(index, temporary_list.pop(0))
                index += 1

    command = input()

print(" ".join(strings))
