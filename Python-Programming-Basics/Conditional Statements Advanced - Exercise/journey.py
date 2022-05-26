budget = float(input())
season = input()

cost = 0
destination = ""
sleeps = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        cost = budget * 0.3
        sleeps = "Camp"
    else:
        cost = budget * 0.7
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = budget * 0.4
        sleeps = "Camp"
    else:
        cost = budget * 0.8
else:
    destination = "Europe"
    cost = budget * 0.9

print(f"Somewhere in {destination}")
print(f"{sleeps} - {cost:.2f}")
