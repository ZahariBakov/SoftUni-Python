size = int(input())
matrix = [list(input()) for _ in range(size)]
removed_knights = 0

moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
)

while True:
    most_attacks = 0
    best_knight_pos = []
    knight_pos = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for move in moves:
                    pos_r = row + move[0]
                    pos_c = col + move[1]

                    if 0 <= pos_r < size and 0 <= pos_c < size:
                        if matrix[pos_r][pos_c] == "K":
                            attacks += 1

                if attacks > most_attacks:
                    best_knight_pos = [row, col]
                    most_attacks = attacks

    if best_knight_pos:
        matrix[best_knight_pos[0]][best_knight_pos[1]] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)
