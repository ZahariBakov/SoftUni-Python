from collections import deque

rows, cols = (int(x) for x in input().split())
snake = deque(map(str, input()))

for row in range(rows):
    current_col = []
    for col in range(cols):
        symbol = snake.popleft()
        current_col.append(symbol)
        snake.append(symbol)

    if row % 2 != 0:
        current_col = reversed(current_col)

    print("".join(current_col))
