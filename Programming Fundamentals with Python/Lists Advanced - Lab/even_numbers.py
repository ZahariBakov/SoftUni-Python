numbers = list(map(int, input().split(", ")))
even_numbers_list = []

for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        even_numbers_list.append(index)

print(even_numbers_list)
