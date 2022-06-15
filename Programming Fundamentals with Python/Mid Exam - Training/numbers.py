numbers = list(map(int, input().split()))

sum = sum(numbers)
elements = len(numbers)
average = sum / elements
top_five = []
found = False

for number in numbers[::]:
    if number > average:
        top_five.append(number)
        found = True
top_five = sorted(top_five, reverse=True)
while len(top_five) > 5:
    top_five.pop()

if found:
    print(" ".join(str(a) for a in top_five))
else:
    print("No")
