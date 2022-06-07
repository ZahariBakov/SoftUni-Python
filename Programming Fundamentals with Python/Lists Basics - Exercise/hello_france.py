items_with_price = input().split("|")
budget = float(input())

profit = 0
money_after_selling = 0

for tokens in items_with_price:
    item = tokens.split("->")[0]
    price = float(tokens.split("->")[1])
    if budget >= price:
        if item == "Clothes":
            if price <= 50:
                budget -= price
                profit += price * 0.4
                print(f"{price * 1.4:.2f}", end=" ")
                money_after_selling += price * 1.4
        elif item == "Shoes":
            if price <= 35:
                budget -= price
                profit += price * 0.4
                money_after_selling += price * 1.4
                print(f"{price * 1.4:.2f}", end=" ")
        else:
            if price <= 20.50:
                budget -= price
                profit += price * 0.4
                money_after_selling += price * 1.4
                print(f"{price * 1.4:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")

if money_after_selling + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")





