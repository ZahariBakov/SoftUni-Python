products = {}

while True:
    command = input()

    if command == "statistics":
        break

    command = command.split(": ")
    if command[0] not in products:
        products[command[0]] = int(command[1])

    else:
        products[command[0]] += int(command[1])

print("Products in stock:")
for (key, value) in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
