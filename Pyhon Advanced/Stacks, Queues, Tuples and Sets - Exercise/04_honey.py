from collections import deque

bees = deque(int(x) for x in input().split())
nectars = list(map(int, input().split()))
operators = deque(input().split())
made_honey = 0

operation = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y

}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = operators.popleft()
    made_honey += abs(operation[operator](bee, nectar))

print(f"Total honey made: {made_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join(map(str, nectars))}")
