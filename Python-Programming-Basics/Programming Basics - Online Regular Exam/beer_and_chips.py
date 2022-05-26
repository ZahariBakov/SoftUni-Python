import math

fan_name = input()
budget = float(input())
beer_number = int(input())
chips_number = int(input())

beer_price = 1.20 * beer_number
chips_price = math.ceil((0.45 * beer_price) * chips_number)
total_price = beer_price + chips_price
difference = abs(total_price - budget)

if total_price <= budget:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")
