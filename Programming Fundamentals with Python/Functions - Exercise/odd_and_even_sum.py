string = input()


def odd_even_sum(text):
    odd_sum = 0
    even_sum = 0
    for char in text:
        digit = int(char)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


print(odd_even_sum(string))

