degrees = int(input())
day_time = input()

outfit = ""
shoes = ""

if day_time == "Morning":
    if degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif degrees < 25:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day_time == "Afternoon":
    if degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degrees < 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"
else:
    outfit = "Shirt"
    shoes = "Moccasins"


print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
