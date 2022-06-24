houses = list(map(int, input().split("@")))
current_position = 0

while True:
    command = input()

    if command == "Love!":
        break

    else:
        step = int(command.split()[1])
        current_position += step

        if current_position >= len(houses):
            current_position = 0

        if houses[current_position] == 0:
            print(f"Place {current_position} already had Valentine's day.")

        else:
            houses[current_position] -= 2

            if houses[current_position] == 0:
                print(f"Place {current_position} has Valentine's day.")

print(f"Cupid's last position was {current_position}.")
count = houses.count(0)
if count < len(houses):
    failed = len(houses) - count
    print(f"Cupid has failed {failed} places.")
else:
    print("Mission was successful.")
