size = int(input())

matrix = []
bunny_pos = []
max_eggs = -999
best_road = []
best_move = None

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    col = input().split()

    if "B" in col:
        bunny_pos = [row, col.index("B")]

    matrix.append(col)

for move, positions in moves.items():
    row, col = [bunny_pos[0] + positions[0], bunny_pos[1] + positions[1]]

    collected_eggs = 0
    road = []

    while 0 <= row < size and 0 <= col < size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        road.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs > max_eggs and road:
        max_eggs = collected_eggs
        best_move = move
        best_road = road

print(best_move)
print(*best_road, sep="\n")
print(max_eggs)
