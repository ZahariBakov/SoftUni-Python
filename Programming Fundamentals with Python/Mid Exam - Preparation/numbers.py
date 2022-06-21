numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)
greater_numbers = []

for number in range(len(numbers)):
    current_number = max(numbers)
    if current_number > average:
        greater_numbers.append(current_number)
        numbers.remove(current_number)
        if len(greater_numbers) == 5:
            break
    else:
        break
if greater_numbers != []:
    greater_numbers = [str(number) for number in greater_numbers]
    print(" ".join(greater_numbers))
else:
    print("No")
