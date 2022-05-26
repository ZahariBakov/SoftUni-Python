import math

number_of_tournaments = int(input())
starting_points = int(input())

tournament_points = 0
winner = 0

for i in range(number_of_tournaments):
    stage_of_the_tournament = input()
    if stage_of_the_tournament == "W":
        tournament_points += 2000
        winner += 1
    elif stage_of_the_tournament == "F":
        tournament_points += 1200
    else:
        tournament_points += 720

final_points = starting_points + tournament_points
average_points = math.floor(tournament_points / number_of_tournaments)

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{winner / number_of_tournaments * 100:.2f}%")
