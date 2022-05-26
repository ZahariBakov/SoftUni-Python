sum = float(input())

sum *= 100
coins = 0

if sum // 200 > 0:
    coins += sum // 200
    sum %= 200
if sum // 100 > 0:
    coins += sum // 100
    sum %= 100
if sum // 50 > 0:
    coins += sum // 50
    sum %= 50
if sum // 20 > 0:
    coins += sum // 20
    sum %= 20
if sum // 10 > 0:
    coins += sum // 10
    sum %= 10
if sum // 5 > 0:
    coins += sum // 5
    sum %= 5
if sum // 2 > 0:
    coins += sum // 2
    sum %= 2
if sum // 1 > 0:
    coins += sum // 1
    sum %= 1

print(int(coins))
