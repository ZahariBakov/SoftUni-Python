def add_heroes(dict):
    current_hero = input().split(" ")
    hero_name = current_hero[0]
    hit_point = int(current_hero[1])
    mana_point = int(current_hero[2])
    heroes[hero_name] = {"HP": hit_point, "MP": mana_point}

    return dict


def heal(dict, name, point):
    if point + dict[name]["HP"] > 100:
        point = 100 - dict[name]["HP"]

    dict[name]["HP"] += point
    print(f"{name} healed for {point} HP!")

    return dict


def recharge(dict, name, point):
    if point + dict[name]["MP"] > 200:
        point = 200 - dict[name]["MP"]

    dict[name]["MP"] += point
    print(f"{name} recharged for {point} MP!")

    return dict


def take_damage(dict, name, point, enemy):
    dict[name]["HP"] -= point

    if dict[name]["HP"] > 0:
        print(f"{name} was hit for {point} HP by {enemy} and now has {dict[name]['HP']} HP left!")

    else:
        del dict[name]
        print(f"{name} has been killed by {enemy}!")

    return dict


def cast_spell(dict, name, point, spell):
    if dict[name]["MP"] >= point:
        dict[name]["MP"] -= point
        print(f"{name} has successfully cast {spell} and now has {dict[name]['MP']} MP!")

    else:
        print(f"{name} does not have enough MP to cast {spell}!")

    return dict


heroes_number = int(input())
heroes = {}

for _ in range(heroes_number):
    add_heroes(heroes)

while True:
    command = input()

    if command == "End":
        break

    command = command.split(" - ")
    hero_name = command[1]
    amount = int(command[2])

    if "Heal" in command:
        heal(heroes, hero_name, amount)

    elif "Recharge" in command:
        recharge(heroes, hero_name, amount)

    elif "TakeDamage" in command:
        attacker = command[3]
        take_damage(heroes, hero_name, amount, attacker)

    elif "CastSpell" in command:
        spell_name = command[3]
        cast_spell(heroes, hero_name, amount, spell_name)

for hero in heroes:
    print(f"{hero}\n  HP: {heroes[hero]['HP']}\n  MP: {heroes[hero]['MP']}")
