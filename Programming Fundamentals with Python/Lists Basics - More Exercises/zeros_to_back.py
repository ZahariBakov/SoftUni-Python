list_of_numbers = input().split(", ")

for num in list_of_numbers:
    list_of_numbers.remove("0")
    list_of_numbers.append("0")

print([int(x) for x in list_of_numbers])
