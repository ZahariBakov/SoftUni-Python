from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
milk_cups = deque(int(x) for x in input().split(", "))
milkshake = 0

while milkshake < 5 and chocolates and milk_cups:
    flag = False
    if chocolates[-1] <= 0:
        chocolates.pop()
        flag  =True
    if milk_cups[0] <= 0:
        milk_cups.popleft()
        flag = True

    if flag:
        continue

    if chocolates[-1] == milk_cups[0]:
        milkshake += 1
        chocolates.pop()
        milk_cups.popleft()
    else:
        milk_cups.append(milk_cups.popleft())
        chocolates[-1] -= 5

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")


print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milk_cups)) if milk_cups else 'empty'}")
