numbers = list(map(int, input().split(" ")))


def even_numbers(x):
    if x % 2 == 0:
        return True
    else:
        return False


filtered_numbers = filter(even_numbers, numbers)
even_list = []

for x in filtered_numbers:
    even_list.append(x)

print(even_list)

