def urgent_func(my_list, item):
    if item not in my_list:
        my_list.insert(0, item)

    return my_list


def unnecessary_func(my_list, item):
    if item in my_list:
        my_list.remove(item)

    return my_list


def correct_func(my_list, old_item, new_item):
    my_list = [new_item if item == old_item else item for item in my_list]

    return my_list


def rearrange_func(my_list, item):
    if item in my_list:
        my_list.remove(item)
        my_list.append(item)

    return my_list


shopping_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        print(", ".join(shopping_list))
        break

    first_element = command.split()[1]

    if "Urgent" in command:
        shopping_list = urgent_func(shopping_list, first_element)

    elif "Unnecessary" in command:
        shopping_list = unnecessary_func(shopping_list, first_element)

    elif "Correct" in command:
        second_element = command.split()[2]
        shopping_list = correct_func(shopping_list, first_element, second_element)

    elif "Rearrange" in command:
        shopping_list = rearrange_func(shopping_list, first_element)
