list_of_string = input().split(" ")
list_of_number = []

for char in list_of_string:
    list_of_number.append(int(char))

command = input()
temporary_list = []

while command != "end":
    current_command = command.split(" ")[0]
    if current_command == "exchange":
        index = int(command.split(" ")[1])
        if index < 0 or index > len(list_of_number) - 1:
            print("Invalid index")
        else:
            for num in range(index + 1):
                temporary_list.append(list_of_number.pop(0))
            for _ in range(index + 1):
                list_of_number.append(temporary_list.pop(0))
    elif current_command == "max":
        second_command = command.split(" ")[1]
        max_num = 0
        max_index = "No matches"
        if second_command == "odd":
            for index in range(len(list_of_number)):
                if list_of_number[index] % 2 != 0:
                    current_num = list_of_number[index]
                    if max_num <= current_num:
                        max_num = current_num
                        max_index = index
        elif second_command == "even":
            for index in range(len(list_of_number)):
                if list_of_number[index] % 2 == 0:
                    current_num = list_of_number[index]
                    if max_num <= current_num:
                        max_num = current_num
                        max_index = index
        print(max_index)
    elif current_command == "min":
        second_command = command.split(" ")[1]
        min_num = 1001
        min_index = "No matches"
        if second_command == "odd":
            for index in range(len(list_of_number)):
                if list_of_number[index] % 2 != 0:
                    current_num = list_of_number[index]
                    if min_num >= current_num:
                        min_num = current_num
                        min_index = index
        elif second_command == "even":
            for index in range(len(list_of_number)):
                if list_of_number[index] % 2 == 0:
                    current_num = list_of_number[index]
                    if min_num >= current_num:
                        min_num = current_num
                        min_index = index
        print(min_index)
    elif current_command == "first" or current_command == "last":
        count = int(command.split(" ")[1])
        if count > len(list_of_number):
            print("Invalid count")
        elif current_command == "first":
            second_command = command.split(" ")[2]
            if second_command == "odd":
                for index in range(len(list_of_number)):
                    if list_of_number[index] % 2 != 0:
                        temporary_list.append(list_of_number[index])
                        if len(temporary_list) > count:
                            temporary_list.pop()
            elif second_command == "even":
                for index in range(len(list_of_number)):
                    if list_of_number[index] % 2 == 0:
                        temporary_list.append(list_of_number[index])
                        if len(temporary_list) > count:
                            temporary_list.pop()
            print(temporary_list)
            temporary_list = []
        elif current_command == "last":
            second_command = command.split(" ")[2]
            if second_command == "odd":
                for index in range(len(list_of_number)):
                    if list_of_number[index] % 2 != 0:
                        temporary_list.append(list_of_number[index])
                        if len(temporary_list) > count:
                            temporary_list.pop(0)
            elif second_command == "even":
                for index in range(len(list_of_number)):
                    if list_of_number[index] % 2 == 0:
                        temporary_list.append(list_of_number[index])
                        if len(temporary_list) > count:
                            temporary_list.pop(0)
            print(temporary_list)
            temporary_list = []

    command = input()

print(list_of_number)
