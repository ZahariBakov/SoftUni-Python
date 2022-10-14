def calculate_position(n, idx):
    if idx < 0:
        idx = size - 1
    elif idx == size:
        idx = 0

    return idx


size = int(input())

field = []
player_position = []
path = []
coins = 0

for row in range(size):
    col = input().split()
    if "P" in col:
        player_position = [row, col.index('P')]
    field.append(col)

path.append(player_position)

while True:
    row, col = player_position
    field[row][col] = "0"
    command = input()
    if command == "up":
        row -= 1
        row = calculate_position(size, row)
    elif command == "down":
        row += 1
        row = calculate_position(size, row)
    elif command == "left":
        col -= 1
        col = calculate_position(size, col)
    elif command == "right":
        col += 1
        col = calculate_position(size, col)

    player_position = [row, col]
    path.append(player_position)

    if field[row][col] == "X":
        if coins > 0:
            coins = coins // 2
        print(f"Game over! You've collected {coins} coins.")
        break

    else:
        coins += int(field[row][col])
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break

print("Your path:")
for el in path:
    print(el)
