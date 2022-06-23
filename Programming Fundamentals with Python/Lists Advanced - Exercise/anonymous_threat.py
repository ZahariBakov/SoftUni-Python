strings = input().split()
command = input()

while command != "3:1":
    if "merge" in command:
        start_index = int(command.split()[1])
        end_index = int(command.split()[2])
        if start_index < 0:
            start_index = 0
        if end_index >= len(strings):
            end_index = len(strings) - 1
        temporary_list_out = []
        for i in range(start_index, end_index + 1):
            if len(strings) > start_index:
                temporary_list_out.append(strings.pop(start_index))
        temporary_list_get = "".join(temporary_list_out)
        strings.insert(start_index, temporary_list_get)
    elif "divide" in command:
        index = int(command.split()[1])
        divider = int(command.split()[2])
        temporary_list_get = list(strings.pop(index))
        numbers_of_characters = len(temporary_list_get) // divider
        temporary_list_out = []
        adding_characters = ""
        length_temporary = len(temporary_list_get)
        for i in range(length_temporary):
            if len(temporary_list_out) < divider:
                adding_characters += temporary_list_get.pop(0)
                if len(adding_characters) == numbers_of_characters:
                    temporary_list_out.append(adding_characters)
                    adding_characters = ""
        if temporary_list_get != []:
            adding_characters = temporary_list_out.pop()
            for i in temporary_list_get:
                adding_characters += temporary_list_get.pop(0)
            temporary_list_out.append(adding_characters)
        if temporary_list_out != []:
            for i in range(divider):
                strings.insert(index, temporary_list_out.pop(0))
                index += 1

    command = input()

print(" ".join(strings))
