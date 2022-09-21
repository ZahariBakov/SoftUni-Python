rows, cols = (int(x) for x in input().split(", "))
matrix = []
max_sum = 0
numbers = []

for _ in range(rows):
    col = list(int(x) for x in input().split(", "))
    matrix.append(col)

for i in range(rows - 1):
    for j in range(cols - 1):
        first = matrix[i][j]
        second = matrix[i][j + 1]
        third = matrix[i + 1][j]
        forth = matrix[i + 1][j + 1]
        result = first + second + third + forth

        if result > max_sum:
            max_sum = result
            numbers= [first, second, third, forth]

print(" ".join(str(x) for x in numbers[:2]))
print(" ".join(str(x) for x in numbers[2:]))
print(max_sum)
