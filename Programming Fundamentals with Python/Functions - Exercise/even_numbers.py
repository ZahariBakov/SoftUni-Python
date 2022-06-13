numbers = list(map(int, input().split(" ")))


def even_numbers(number):
    if number % 2 == 0:
        return True

    return False


filtered_numbers = list(filter(even_numbers, numbers))

print(filtered_numbers)


