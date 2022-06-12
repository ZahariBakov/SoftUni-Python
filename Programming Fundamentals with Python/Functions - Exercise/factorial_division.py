first_number = int(input())
second_number = int(input())


def factorial(a):
    for num in range(a - 1, 0, -1):
        a *= num

    return a


first_factorial = factorial(first_number)
second_number = factorial(second_number)

final_result = first_factorial / second_number
print(f"{final_result:.2f}")

