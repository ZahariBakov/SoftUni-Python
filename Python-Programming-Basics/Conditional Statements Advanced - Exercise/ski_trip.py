tour_days = int(input())
type_of_room = input()
rating = input()

tour_nights = tour_days - 1
price = 0

if type_of_room == "room for one person":
    price = tour_nights * 18
elif type_of_room == "apartment":
    price = tour_nights * 25
    if tour_days > 15:
        price *= 0.5
    elif tour_days > 9:
        price *= 0.65
    else:
        price *= 0.7
else:
    price = tour_nights * 35
    if tour_days > 15:
        price *= 0.8
    elif tour_days > 9:
        price *= 0.85
    else:
        price *= 0.9

if rating == "positive":
    price *= 1.25
else:
    price *= 0.9

print(f"{price:.2f}")
