words = input().split()

word = [x for x in words if len(x) % 2 == 0]
print(*word, sep= "\n")
