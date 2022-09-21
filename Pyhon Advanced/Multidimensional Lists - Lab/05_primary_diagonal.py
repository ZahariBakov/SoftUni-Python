rows = int(input())
matrix = []
result = 0

for idx in range(rows):
    col = [int(x) for x in input().split()]
    result += col[idx]

print(result)
