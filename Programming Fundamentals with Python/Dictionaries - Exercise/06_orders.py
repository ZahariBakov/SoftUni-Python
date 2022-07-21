products = {}

while True:
    command = input()

    if command == "buy":
        break

    current_product = command.split(" ")[0]
    price = float(command.split(" ")[1])
    quantity = int(command.split(" ")[2])

    if current_product not in products:
        products[current_product] = [price, quantity]
    else:
        if products[current_product][0] != price:
            products[current_product][0] = price
        products[current_product][1] += quantity

for key in products:
    total_price = products[key][0] * products[key][1]
    print(f"{key} -> {total_price:.2f}")
