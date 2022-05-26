numbers = int(input())

min_number = " "
max_number = " "

for i in range(numbers):
    current_number = int(input())
    if i == 0:
        min_number = current_number
        max_number = current_number
    if min_number > current_number:
        min_number = current_number
    if max_number < current_number:
        max_number = current_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
