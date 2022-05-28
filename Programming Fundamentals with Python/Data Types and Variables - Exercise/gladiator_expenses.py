lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_armor = 0
repair_cost = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        trashed_helmet += 1
    if fight % 3 == 0:
        trashed_sword += 1
        if fight % 2 == 0:
            trashed_shield += 1
            if trashed_shield % 2 == 0:
                trashed_armor += 1

repair_cost += trashed_helmet * helmet_price
repair_cost += trashed_sword * sword_price
repair_cost += trashed_shield * shield_price
repair_cost += trashed_armor * armor_price

print(f"Gladiator expenses: {repair_cost:.2f} aureus")
