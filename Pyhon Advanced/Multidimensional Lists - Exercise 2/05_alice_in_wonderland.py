size = int(input())

matrix = []
alice_pos = []
collected_tea_bags = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    col = input().split()

    matrix.append(col)

    if "A" in col:
        alice_pos = [row, col.index("A")]
        matrix[alice_pos[0]][alice_pos[1]] = "*"

while collected_tea_bags < 10:
    command = input()

    alice_pos[0] += moves[command][0]
    alice_pos[1] += moves[command][1]

    if not (0 <= alice_pos[0] < size and 0 <= alice_pos[1] < size):
        break

    if matrix[alice_pos[0]][alice_pos[1]] == "R":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        break

    elif matrix[alice_pos[0]][alice_pos[1]].isdigit():
        collected_tea_bags += int(matrix[alice_pos[0]][alice_pos[1]])

    matrix[alice_pos[0]][alice_pos[1]] = "*"

if collected_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

print(*[' '.join(row) for row in matrix], sep="\n")
