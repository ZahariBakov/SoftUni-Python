movie_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

total_price = 0

if destination == "Dubai":
    if season == "Winter":
        total_price = 45000 * number_of_days
    else:
        total_price = 40000 * number_of_days
    total_price *= 0.7
elif destination == "Sofia":
    if season == "Winter":
        total_price = 17000 * number_of_days
    else:
        total_price = 12500 * number_of_days
    total_price *= 1.25
else:
    if season == "Winter":
        total_price = 24000 * number_of_days
    else:
        total_price = 20250 * number_of_days

difference = abs(total_price - movie_budget)

if total_price > movie_budget:
    print(f"The director needs {difference:.2f} leva more!")
else:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
