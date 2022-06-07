fire_and_cell = input().split("#")
water = int(input())

total_fire = 0
print("Cells:")

for tokens in fire_and_cell:
    type_of_fire = tokens.split(" = ")[0]
    fire_level = int(tokens.split(" = ")[1])
    if water >= fire_level:
        if type_of_fire == "High":
            if 81 <= fire_level <= 125:
                water -= fire_level
                total_fire += fire_level
                print(f"- {fire_level}")
        elif type_of_fire == "Medium":
            if 51 <= fire_level <= 80:
                water -= fire_level
                total_fire += fire_level
                print(f"- {fire_level}")
        else:
            if 1 <= fire_level <= 50:
                water -= fire_level
                total_fire += fire_level
                print(f"- {fire_level}")

effort = f"{0.25 * total_fire:.2f}"
print(f"Effort: {effort}")
print(f"Total Fire: {total_fire}")

