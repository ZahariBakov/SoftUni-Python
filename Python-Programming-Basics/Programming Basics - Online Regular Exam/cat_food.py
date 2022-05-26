cat_number = int(input())

small_cat = 0
big_cat = 0
huge_cat = 0
total_food = 0

for current_cat in range(cat_number):
    eat_food = float(input())
    total_food += eat_food
    if eat_food < 200:
        small_cat += 1
    elif eat_food < 300:
        big_cat += 1
    else:
        huge_cat += 1

food_price = total_food / 1000 * 12.45

print(f"Group 1: {small_cat} cats.")
print(f"Group 2: {big_cat} cats.")
print(f"Group 3: {huge_cat} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")
