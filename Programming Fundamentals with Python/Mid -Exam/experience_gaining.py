tank_points = float(input())
battle_numbers = int(input())

current_points = 0

for battle in range(1, battle_numbers + 1):
    points_of_battle = float(input())

    current_points += points_of_battle

    if battle % 3 == 0:
        current_points += points_of_battle * 0.15

    if battle % 5 == 0:
        current_points -= points_of_battle * 0.1

    if battle % 15 == 0:
        current_points += points_of_battle * 0.05

    if current_points >= tank_points:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break

if current_points < tank_points:
    print(f"Player was not able to collect the needed experience, {tank_points - current_points:.2f} more needed.")
