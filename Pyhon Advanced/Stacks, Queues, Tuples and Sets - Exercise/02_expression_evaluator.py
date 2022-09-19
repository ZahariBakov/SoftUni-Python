import math
from collections import deque

numbers_and_commands = deque(input().split())

number = deque()
result = int(numbers_and_commands.popleft())

while numbers_and_commands:
    el = numbers_and_commands.popleft()

    if el in "+-/*":
        if el == "+":
            while number:
                result += number.popleft()
        elif el == "-":
            while number:
                result = math.floor(result - number.popleft())
        elif el == "/":
            while number:
                result //= number.popleft()
        else:
            while number:
                result *= number.popleft()

    else:
        number.append(int(el))

print(result)
