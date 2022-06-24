def potion_func(blood, potion_strength):
    if blood + potion_strength > 100:
        potion_strength = 100 - blood

    blood += potion_strength

    print(f"You healed for {potion_strength} hp.")
    print(f"Current health: {blood} hp.")

    return blood


def chest_func(money, adding_money):
    money += adding_money

    print(f"You found {adding_money} bitcoins.")

    return money


def monster_func(power, blood):
    blood -= power

    return blood


health = 100
bitcoins = 0
best_room = ""

rooms = input().split("|")

for room in rooms:
    name = room.split()[0]
    second_elements = int(room.split()[1])

    if name == "potion":
        health = potion_func(health, second_elements)

    elif name == "chest":
        bitcoins = chest_func(bitcoins, second_elements)

    else:
        health = monster_func(second_elements, health)

        if health <= 0:
            print(f"You died! Killed by {name}.")
            best_room = rooms.index(room) + 1
            print(f"Best room: {best_room}")
            break

        else:
            print(f"You slayed {name}.")

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
