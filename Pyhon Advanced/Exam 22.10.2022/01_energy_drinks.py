from collections import deque

caffeine = [int(x) for x in input().split(", ")]
drinks = deque([int(y) for y in input().split(", ")])
total = 0

while caffeine and drinks:
    current_caffeine = caffeine.pop() * drinks[0]

    if current_caffeine + total <= 300:
        total += current_caffeine
        drinks.popleft()
    else:
        drinks.append(drinks.popleft())
        total -= 30
        if total < 0:
            total = 0

if drinks:
    print(f"Drinks left: {', '.join(str(z) for z in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total} mg caffeine.")
