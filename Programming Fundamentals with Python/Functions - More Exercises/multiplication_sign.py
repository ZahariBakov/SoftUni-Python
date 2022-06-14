def multiplication(a, b, c):
    negative = 0
    list_of_numbers = [a, b, c]
    if 0 in list_of_numbers:
        return "zero"
    if a < 0:
        negative += 1
    if b < 0:
        negative += 1
    if c < 0:
        negative += 1
    if negative % 2 != 0:
        return "negative"
    return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication(first_number, second_number, third_number))
