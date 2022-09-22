rows = int(input())
primary = []
secondary = []
matrix = []

for i in range(rows):
    col = list(int(x) for x in input().split(", "))
    primary.append(col[i])
    j = -(1 + i)
    secondary.append(col[j])

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(y) for y in secondary)}. Sum: {sum(secondary)}")

