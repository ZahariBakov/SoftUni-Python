to_do_list = [0] * 10

command = input()

while command != "End":
    priority = int(command.split("-")[0]) - 1
    note = command.split("-")[1]
    to_do_list.pop(priority)
    to_do_list.insert(priority, note)

    command = input()

to_do_list = [x for x in to_do_list if x != 0]

print(to_do_list)
