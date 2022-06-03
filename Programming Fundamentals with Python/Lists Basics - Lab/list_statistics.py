numbers_of_integers = int(input())

positive = []
negative = []

for _ in range(numbers_of_integers):
    current_integer = int(input())
    if current_integer >= 0:
        positive.append(current_integer)
    else:
        negative.append(current_integer)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")

