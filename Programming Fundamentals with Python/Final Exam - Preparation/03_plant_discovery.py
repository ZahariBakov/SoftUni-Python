def plants(plants):
    lines = int(input())

    for _ in range(lines):
        plant = input().split("<->")
        name = plant[0]
        rarity = int(plant[1])

        if name not in plants:
            plants[name] = {"rarity": rarity, "rating": []}

        else:
            plants[name]["rarity"] = rarity

    return plants


def plants_rating(plants):

    while True:
        command = input().split(": ")

        if command[0] == "Exhibition":
            break

        current_command = command[1].split(" - ")
        name = current_command[0]

        if name not in plants:
            print("error")
            continue

        elif command[0] == "Rate":
            rating = int(current_command[1])
            plants[name]["rating"].append(rating)

        elif command[0] == "Update":
            new_rarity = int(current_command[1])
            plants[name]["rarity"] = new_rarity

        elif command[0] == "Reset":
            plants[name]["rating"].clear()

    return plants


collections_of_plants = {}

plants(collections_of_plants)
plants_rating(collections_of_plants)

print("Plants for the exhibition:")

for plant in collections_of_plants:

    if sum(collections_of_plants[plant]["rating"]) > 0 and len(collections_of_plants[plant]["rating"]) > 0:
        average_rating = sum(collections_of_plants[plant]["rating"]) / len(collections_of_plants[plant]["rating"])

    else:
        average_rating = 0
    rarity = collections_of_plants[plant]["rarity"]

    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
