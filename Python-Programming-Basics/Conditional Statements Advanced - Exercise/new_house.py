flower_type = input()
flower_numbers = int(input())
budget = int(input())

cost = 0

if flower_type == "Roses":
    cost = 5 * flower_numbers
    if flower_numbers > 80:
        cost *= 0.9
elif flower_type == "Dahlias":
    cost = 3.80 * flower_numbers
    if flower_numbers > 90:
        cost *= 0.85
elif flower_type == "Tulips":
    cost = 2.80 * flower_numbers
    if flower_numbers > 80:
        cost *= 0.85
elif flower_type == "Narcissus":
    cost = 3 * flower_numbers
    if flower_numbers < 120:
        cost *= 1.15
else:
    cost = 2.50 * flower_numbers
    if flower_numbers < 80:
        cost *= 1.20

difference = abs(budget - cost)

if budget >= cost:
    print(f"Hey, you have a great garden with {flower_numbers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
