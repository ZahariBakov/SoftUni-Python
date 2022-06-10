def add_and_subtract(a, b, c):
    def sum_numbers(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    sum = sum_numbers(first_num, second_num)
    result = subtract(sum, third_num)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
