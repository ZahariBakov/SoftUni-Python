first_list = input().split(" ")

second_list = []

for num in first_list:
    new_num = -1 * int(num)
    second_list.append(new_num)

print(second_list)
