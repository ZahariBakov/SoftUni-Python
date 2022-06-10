first_number = int(input())
second_number = int(input())
third_number = int(input())


def smallest(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c


print(smallest(first_number, second_number, third_number))
