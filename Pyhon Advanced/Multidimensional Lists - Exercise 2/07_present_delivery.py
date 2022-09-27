presents = int(input())
size = int(input())

neighborhood = []
santa_position = []
nice_kids_visited = 0
total_nice_kids = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    col = input().split()

    neighborhood.append(col)

    if "S" in col:
        santa_position = [row, col.index("S")]
        neighborhood[row][santa_position[1]] = "-"

    total_nice_kids += col.count("V")

command = input()

while command != "Christmas morning":
    row = santa_position[0] + moves[command][0]
    col = santa_position[1] + moves[command][1]

    if 0 <= row < size and 0 <= col < size:
        if neighborhood[row][col] == "V":
            presents -= 1
            nice_kids_visited += 1

        elif neighborhood[row][col] == "C":
            for move in moves:
                r = row + moves[move][0]
                c = col + moves[move][1]

                if neighborhood[r][c] != "-":
                    if neighborhood[r][c] == "V":
                        nice_kids_visited += 1
                    presents -= 1
                    neighborhood[r][c] = "-"

                    if presents == 0:
                        break

        neighborhood[row][col] = "-"
        santa_position[0] = row
        santa_position[1] = col

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighborhood[santa_position[0]][santa_position[1]] = "S"

if not presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

print(*[' '.join(row) for row in neighborhood], sep="\n")

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
