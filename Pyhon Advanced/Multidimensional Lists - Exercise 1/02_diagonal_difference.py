rows = int(input())
primary = []
secondary = []
matrix = []

for i in range(rows):
    col = list(int(x) for x in input().split())
    primary.append(col[i])
    j = -(1 + i)
    secondary.append(col[j])

print(abs(sum(primary) - sum(secondary)))
