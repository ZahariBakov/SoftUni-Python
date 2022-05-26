food_kg = int(input())
command = input()
food_gr = food_kg * 1000
eating_food = 0

while command != "Adopted":
    eat_food = int(command)
    eating_food += eat_food
    command = input()

difference = abs(food_gr - eating_food)

if food_gr >= eating_food:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
