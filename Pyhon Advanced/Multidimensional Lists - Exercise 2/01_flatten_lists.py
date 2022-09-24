string = input().split("|")

result = []

for sub in string[::-1]:
    result.extend(sub.split())

print(*result)
