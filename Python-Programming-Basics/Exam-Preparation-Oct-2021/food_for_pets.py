days = int(input())
total_pet_food = float(input())

total_dog_food = 0
total_cat_food = 0
biscuits = 0

for current_day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    if current_day % 3 == 0:
        biscuits += 0.1 * (dog_food + cat_food)

total_eaten_food = total_cat_food + total_dog_food
dog_eaten_percent = total_dog_food / total_eaten_food * 100
cat_eaten_percent = total_cat_food / total_eaten_food * 100
eaten_food_percent = total_eaten_food / total_pet_food * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{dog_eaten_percent:.2f}% eaten from the dog.")
print(f"{cat_eaten_percent:.2f}% eaten from the cat.")
