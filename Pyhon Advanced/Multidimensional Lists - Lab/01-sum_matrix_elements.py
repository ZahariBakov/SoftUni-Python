rows, cols = (int(x) for x in input().split(", "))
result = 0
matrix = []

for _ in range(rows):
    row = list(int(x) for x in input().split(", "))
    matrix.append(row)
    result += sum(row)

print(result)
print(matrix)
