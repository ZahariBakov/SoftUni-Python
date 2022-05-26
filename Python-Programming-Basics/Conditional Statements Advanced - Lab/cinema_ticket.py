day = input()

price = 12

if day == "Wednesday" or day == "Thursday":
    price += 2
elif day == "Saturday" or day == "Sunday":
    price += 4

print(price)
