size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

symbol = input()
find = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            find = True
            break

    if find:
        break

else:
    print(f"{symbol} does not occur in the matrix")
