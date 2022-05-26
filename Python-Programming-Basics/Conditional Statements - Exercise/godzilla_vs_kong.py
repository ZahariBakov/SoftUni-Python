movie_budget = float(input())
extras_number = int(input())
price_one_wear = float(input())

decor = movie_budget * 0.1
wear_price = extras_number * price_one_wear
if extras_number > 150:
    wear_price -= wear_price * 0.1

total_price = decor + wear_price
difference = abs(movie_budget - total_price)

if total_price > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
