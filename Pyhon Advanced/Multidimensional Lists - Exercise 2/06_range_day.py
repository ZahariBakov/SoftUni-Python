size = 5

all_targets = 0
shot_targets = 0
shot_targets_pos = []
my_pos = []
field = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    col = input().split()
    field.append(col)

    if "A" in col:
        my_pos = [row, col.index("A")]
        field[row][my_pos[1]] = "."

    all_targets += col.count('x')

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == "move":

        row = my_pos[0] + (moves[command[1]][0] * int(command[2]))
        col = my_pos[1] + (moves[command[1]][1] * int(command[2]))

        if not (0 <= row < size and 0 <= col < size):
            continue

        if field[row][col] == ".":
            my_pos[0] = row
            my_pos[1] = col

    elif command[0] == "shoot":
        move = command[1]
        row = my_pos[0] + moves[move][0]
        col = my_pos[1] + moves[move][1]

        while 0 <= row < size and 0 <= col < size:
            if field[row][col] == "x":
                field[row][col] = "."
                shot_targets_pos.append([row, col])
                shot_targets += 1
                break

            row += moves[move][0]
            col += moves[move][1]

        if shot_targets == all_targets:
            print(f"Training completed! All {all_targets} targets hit.")
            break

if shot_targets < all_targets:
    print(f"Training not completed! {all_targets - shot_targets} targets left.")

print(*(target for target in shot_targets_pos), sep="\n")
