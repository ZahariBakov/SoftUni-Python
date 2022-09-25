from collections import deque

size = int(input())
matrix = []
total_damage = 0
alive_cells = 0

for row in range(size):
    col = list(int(x) for x in input().split())
    matrix.append(col)

bombs = deque(input().split())

while bombs:
    bomb_row, bomb_col = bombs.popleft().split(",")
    bomb_row = int(bomb_row)
    bomb_col = int(bomb_col)
    if matrix[bomb_row][bomb_col] > 0:
        bomb_power = matrix[bomb_row][bomb_col]
        start_row_idx = bomb_row - 1
        if start_row_idx < 0:
            start_row_idx = 0
        end_row_idx = bomb_row + 1
        if end_row_idx > size - 1:
            end_row_idx = size - 1
        start_col_idx = bomb_col - 1
        if start_col_idx < 0:
            start_col_idx = 0
        end_col_idx = bomb_col + 1
        if end_col_idx > size - 1:
            end_col_idx = size - 1

        for row in range(start_row_idx, end_row_idx + 1):
            for col in range(start_col_idx, end_col_idx + 1):
                if matrix[row][col] > 0:
                    matrix[row][col] -= bomb_power

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            total_damage += matrix[row][col]
            alive_cells += 1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {total_damage}")

for row in range(size):
    print(*matrix[row])
