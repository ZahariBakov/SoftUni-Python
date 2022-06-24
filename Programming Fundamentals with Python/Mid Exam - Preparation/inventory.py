def collect_func(current_list, element):
    if element not in current_list:
        current_list.append(element)

    return current_list


def drop_func(current_list, element):
    if element in current_list:
        current_list.remove(element)

    return current_list


def combine_func(current_list, old, new):
    if old in current_list:
        index = current_list.index(old)
        current_list.insert(index + 1, new_item)

    return current_list


def renew_func(current_list, element):
    if element in current_list:
        current_list.remove(element)
        current_list.append(element)

    return current_list


inventory = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        print(", ".join(inventory))
        break

    elif "Collect" in command:
        item = command.split(" - ")[1]
        collect_func(inventory, item)

    elif "Drop" in command:
        item = command.split(" - ")[1]
        drop_func(inventory, item)

    elif "Combine" in command:
        old_new_item = command.split(" - ")[1]
        old_item = old_new_item.split(":")[0]
        new_item = old_new_item.split(":")[1]
        combine_func(inventory, old_item, new_item)

    elif "Renew" in command:
        item = command.split(" - ")[1]
        renew_func(inventory, item)
