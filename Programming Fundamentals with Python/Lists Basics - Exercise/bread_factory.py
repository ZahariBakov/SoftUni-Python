events = input().split("|")
energy = 100
money = 100

closed = False

for element in events:
    current_event = element.split("-")[0]
    points = int(element.split("-")[1])
    if current_event == "rest":
        if energy + points > 100:
            gained_energy = 100 - energy
        else:
            gained_energy = points
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif current_event == "order":
        if energy >= 30:
            energy -= 30
            money += points
            print(f"You earned {points} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if money >= points:
            money -= points
            print(f"You bought {current_event}.")
        else:
            print(f"Closed! Cannot afford {current_event}.")
            closed = True
            break

if not closed:
    print("Day completed!")
    print(f"Coins: {money}")
    print(f"Energy: {energy}")
