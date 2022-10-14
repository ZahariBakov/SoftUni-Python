def checking_index(n, num):
    if num < 0:
        num = size - 1
    elif num == size:
        num = 0

    return num


size = int(input())

field = []
starting_position = []
path = []
coins = 0

for row in range(size):
    col = input().split()
    if "P" in col:
        starting_position.append(row)
        starting_position.append(col.index('P'))
    field.append(col)

path.append(starting_position)
row = starting_position[0]
col = starting_position[1]
field[row][col] = 0

while True:
    command = input()
    if command == "up":
        row -= 1
        row = checking_index(size, row)
    elif command == "down":
        row += 1
        row = checking_index(size, row)
    elif command == "left":
        col -= 1
        col = checking_index(size, col)
    elif command == "right":
        col += 1
        col = checking_index(size, col)

    current_position = [row, col]
    path.append(current_position)

    if field[row][col] == "X":
        if coins > 0:
            coins = int(coins / 2)
        print(f"Game over! You've collected {coins} coins.")
        break

    else:
        coins += int(field[row][col])
        field[row][col] = 0
        if coins >= 100:
            print(f"You won! You've collected {coins} coins.")
            break

print("Your path:")
for el in path:
    print(el)
