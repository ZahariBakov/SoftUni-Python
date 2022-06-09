operator = input()
first_number = int(input())
second_number = int(input())


def calculator(num1, num2, operation):
    result = 0
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1 // num2
    elif operator == "add":
        result = num1 + num2
    elif operator == "subtract":
        result = num1 - num2
    return result


print(calculator(first_number, second_number, operator))
