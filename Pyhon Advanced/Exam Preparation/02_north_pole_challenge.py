def moving(r, c, matrix, decorations, gifts, cookies):
    if matrix[r][c] != "." and matrix[r][c] != "x":
        if matrix[r][c] == "D":
            decorations += 1
        elif matrix[r][c] == "G":
            gifts += 1
        elif matrix[r][c] == "C":
            cookies += 1
        matrix[r][c] = "x"
    else:
        matrix[r][c] = "x"

    return r, c, matrix, decorations, gifts, cookies


rows, columns = [int(x) for x in input().split(", ")]
field = []
items = 0
decorations = 0
gifts = 0
cookies = 0
total_items = 0
player_position = []

for row in range(rows):
    col = input().split()
    field.append(col)
    if "Y" in col:
        player_position = [row, col.index("Y")]
    items += col.count("D")
    items += col.count("G")
    items += col.count("C")

field[player_position[0]][player_position[1]] = "x"
row = player_position[0]
col = player_position[1]

command = input()

while command != "End":
    direction, steps = command.split("-")
    if direction == "up":
        for _ in range(int(steps)):
            row -= 1
            if row < 0:
                row = rows - 1
            row, col, field, decorations, gifts, cookies = moving(row, col, field, decorations, gifts, cookies)
            total_items = decorations + gifts + cookies
            if total_items == items:
                break
    elif direction == "down":
        for _ in range(int(steps)):
            row += 1
            if row == rows:
                row = 0
            row, col, field, decorations, gifts, cookies = moving(row, col, field, decorations, gifts, cookies)
            total_items = decorations + gifts + cookies
            if total_items == items:
                break
    elif direction == "left":
        for _ in range(int(steps)):
            col -= 1
            if col < 0:
                col = columns - 1
            row, col, field, decorations, gifts, cookies = moving(row, col, field, decorations, gifts, cookies)
            total_items = decorations + gifts + cookies
            if total_items == items:
                break
    elif direction == "right":
        for _ in range(int(steps)):
            col += 1
            if col == columns:
                col = 0
            row, col, field, decorations, gifts, cookies = moving(row, col, field, decorations, gifts, cookies)
            total_items = decorations + gifts + cookies
            if total_items == items:
                break
    if total_items == items:
        print("Merry Christmas!")
        break

    command = input()

field[row][col] = "Y"

print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
for row in field:
    print(*row)
