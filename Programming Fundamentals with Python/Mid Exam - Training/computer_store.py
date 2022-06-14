command = input()

price_without_tax = 0
tax = 0
total_price = 0

while True:
    if command == "special" or command == "regular":
        break
    price = float(command)
    if price < 0:
        print("Invalid price!")
        command = input()
        continue
    price_without_tax += price
    command = input()

tax = 0.2 * price_without_tax
total_price = tax + price_without_tax

if command == "special":
    total_price -= 0.1 * total_price

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")

