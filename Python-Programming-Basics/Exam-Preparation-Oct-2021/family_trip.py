budget = float(input())
nights_number = int(input())
price_per_nights = float(input())
percent_additional_costs = int(input())

if nights_number > 7:
    price_per_nights *= 0.95

nights_price = price_per_nights * nights_number
additional_costs = percent_additional_costs * budget / 100
total_price = nights_price + additional_costs
difference = abs(total_price - budget)
if total_price > budget:
    print(f"{difference:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
