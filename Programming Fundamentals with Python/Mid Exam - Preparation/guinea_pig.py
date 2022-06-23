food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
pigs_kilos = float(input())

go_to_pet_store = False

for day in range(1, 31):
    food_quantity -= 0.3
    if food_quantity <= 0.3:
        go_to_pet_store = True
        break

    if day % 2 == 0:
        hay_for_the_day = 0.05 * food_quantity
        hay_quantity -= hay_for_the_day
        if hay_quantity <= hay_for_the_day:
            go_to_pet_store = True
            break

    if day % 3 == 0:
        cover_for_the_day = pigs_kilos / 3
        cover_quantity -= cover_for_the_day
        if cover_quantity <= cover_for_the_day:
            go_to_pet_store = True
            break

if go_to_pet_store:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
