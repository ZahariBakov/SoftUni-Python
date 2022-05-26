budget = int(input())
season = input()
fisherman_number = int(input())

cost = 0

if season == "Spring":
    cost = 3000
elif season == "Summer" or season == "Autumn":
    cost = 4200
else:
    cost = 2600

if fisherman_number < 7:
        cost *= 0.9
elif fisherman_number < 12:
        cost *= 0.85
else:
        cost *= 0.75

if season != "Autumn":
    if fisherman_number % 2 == 0:
        cost *= 0.95

difference = abs(budget - cost)

if budget >= cost:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
