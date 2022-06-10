numbers = list(map(int, input().split(" ")))


def even_numbers(number):
    if number % 2 == 0:
        return True

    return False


filtered_numbers = filter(even_numbers, numbers)
even_list = list(filtered_numbers)

print(even_list)

