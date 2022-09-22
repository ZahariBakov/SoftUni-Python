from sys import maxsize

rows, cols = (int(x) for x in input().split())
matrix = [input().split() for _ in range(rows)]
maximal = -maxsize
numbers = []

for row in range(rows - 2):
    for col in range(cols - 2):
        square = [
            list(map(int, [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]])),
            list(map(int, [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]])),
            list(map(int, [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]))
        ]
        current_sum = sum(sum(square, []))

        if current_sum > maximal:
            maximal = current_sum
            numbers = square
print(f"Sum = {maximal}")
for i in range(3):
    print(" ".join(map(str, numbers[i])))
