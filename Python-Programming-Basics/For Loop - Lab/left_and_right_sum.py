numbers = int(input())

left_sum = 0
right_sum = 0

for i in range(numbers):
    current_number = int(input())
    left_sum += current_number

for i in range(numbers):
    current_number = int(input())
    right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
