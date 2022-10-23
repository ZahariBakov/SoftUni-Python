size = int(input())
race_car_number = input()

race_track = []
tunnels = []
kilometers = 0

for row in range(size):
    col = input().split()
    race_track.append(col)
    if "T" in col:
        tunnels.append([row, col.index("T")])

command = input()
row, col = 0, 0

while command != "End":
    if command == "up":
        row -= 1
    elif command == "down":
        row += 1
    elif command == "left":
        col -= 1
    elif command == "right":
        col += 1

    if race_track[row][col] == "T":
        race_track[row][col] = "."
        kilometers += 30
        if [row, col] == tunnels[-1]:
            el = tunnels.pop(0)
            row, col = el[0], el[1]
        else:
            el = tunnels.pop()
            row, col = el[0], el[1]
        race_track[row][col] = "."
    elif race_track[row][col] == "F":
        kilometers += 10
        print(f"Racing car {race_car_number} finished the stage!")
        break
    else:
        kilometers += 10

    command = input()

race_track[row][col] = "C"

if command == "End":
    print(f"Racing car {race_car_number} DNF.")

print(f"Distance covered {kilometers} km.")
for row in race_track:
    print(*row, sep='')
