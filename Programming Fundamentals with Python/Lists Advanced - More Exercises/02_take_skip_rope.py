string = input()

number_list = []
non_number_list = []

for char in string:
    if char.isdigit():
        number_list.append(int(char))

    else:
        non_number_list.append(char)

taken_list = [number_list[x] for x in range(len(number_list)) if x % 2 == 0]
skip_list = [number_list[x] for x in range(len(number_list)) if x % 2 != 0]

result = ""

for i in range(len(taken_list)):
    take = taken_list[i]
    skip = skip_list[i]
    for y in range(take):
        result += non_number_list.pop(0)
        if not non_number_list:
            break

    if non_number_list:
        for j in range(skip):
            non_number_list.pop(0)
            if not non_number_list:
                break

    if not non_number_list:
        break

print(result)
