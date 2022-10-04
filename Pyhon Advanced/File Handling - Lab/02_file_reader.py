file = open('numbers.txt')
result = 0

for line in file:
    result += int(line.strip())

print(result)
