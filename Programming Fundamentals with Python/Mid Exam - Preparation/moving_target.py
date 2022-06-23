def shoot_func(current_targets, i, power):
    if 0 <= i < len(current_targets):
        current_targets[i] -= power
        if current_targets[i] <= 0:
            current_targets.pop(i)

    return current_targets


def add_func(current_targets, i, value):
    if 0 <= i < len(current_targets):
        current_targets.insert(i, value)
    else:
        print("Invalid placement!")

    return current_targets


def strike_func(current_targets, i, radius):
    starting_point = i - radius
    final_point = i + radius
    if 0 <= starting_point and final_point < len(current_targets):
        for removing_target in range(starting_point, final_point + 1):
            current_targets.pop(starting_point)
    else:
        print("Strike missed!")

    return current_targets


targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        print("|".join([str(x) for x in targets]))
        break
    else:
        index = int(command.split()[1])
        second_element = int(command.split()[2])

        if "Shoot" in command:
            shoot_func(targets, index, second_element)

        elif "Add" in command:
            add_func(targets, index, second_element)

        elif "Strike" in command:
            strike_func(targets, index, second_element)
