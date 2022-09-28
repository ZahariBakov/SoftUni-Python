def operate(operator, *args):
    def add(*args):
        result = 0
        for el in args:
            result += el

        return result

    def multiply(*args):
        result = 1
        for el in args:
            result *= el

        return result

    def division(*args):
        result = ''
        for el in args:
            if not result:
                result = el
            else:
                result /= el

        return result

    def subtraction(*args):
        result = ''
        for el in args:
            if not result:
                result = el
            else:
                result -= el

        return result

    if operator == "+":
        result = add(*args)
    elif operator == "-":
        result = subtraction(*args)
    elif operator == "*":
        result = multiply(*args)
    else:
        result = division(*args)

    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("-", 3, 2))
print(operate("/", 6, 2))