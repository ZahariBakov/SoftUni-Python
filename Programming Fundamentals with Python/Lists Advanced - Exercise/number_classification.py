numbers = list(map(int, input().split(", ")))
positive = [str(x) for x in numbers if x >= 0]
negative = [str(x) for x in numbers if x < 0]
even = [str(x) for x in numbers if x % 2 == 0]
odd = [str(x) for x in numbers if x % 2 != 0]

print("Positive: " + ", ".join(positive))
print("Negative: " + ", ".join(negative))
print("Even: " + ", ".join(even))
print("Odd: " + ", ".join(odd))
