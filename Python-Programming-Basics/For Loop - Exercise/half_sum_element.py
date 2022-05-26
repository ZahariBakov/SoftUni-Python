numbers = int(input())

max_number = " "
sum = 0

for i in range(numbers):
    current_number = int(input())
    sum += current_number
    if i == 0:
        max_number = current_number
    if max_number < current_number:
        max_number = current_number

sum -= max_number
if max_number == sum:
    print("Yes")
    print(f"Sum = {sum}")
else:
    difference = abs(max_number - sum)
    print("No")
    print(f"Diff = {difference}")
