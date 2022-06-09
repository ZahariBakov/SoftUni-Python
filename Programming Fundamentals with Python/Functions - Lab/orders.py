product = input()
quantity = int(input())


def bills(text, num):
    price = 0
    result = 0
    if text == "coffee":
        price = 1.50
    elif text == "water":
        price = 1
    elif text == "coke":
        price = 1.40
    elif text == "snacks":
        price = 2
    result = price * num
    return f"{result:.2f}"


print(bills(product, quantity))
