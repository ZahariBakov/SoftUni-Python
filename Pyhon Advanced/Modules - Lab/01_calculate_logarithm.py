from math import log

numbers = int(input())
base = input()

# if base == "natural":
#     print(f"{log(numbers):.2f}")
# else:
#     print(f"{log(numbers, int(base)):.2f}")

result = log(numbers) if base == "natural" else log(numbers, int(base))

print(f"{result:.2f}")
