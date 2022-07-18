elements_list = input().split(" ")

bakery_dict = {}

for i in range(0, len(elements_list), 2):
    bakery_dict[elements_list[i]] = int(elements_list[i + 1])

print(bakery_dict)
