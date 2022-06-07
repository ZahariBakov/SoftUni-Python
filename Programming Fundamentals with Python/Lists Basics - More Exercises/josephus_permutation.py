numbers = input().split(" ")
index = int(input())

executed_people = []
current_index = 0

while len(numbers) > 0:
    current_index += index - 1
    if current_index >= len(numbers):
        current_index %= len(numbers)
    executed_people.append(numbers.pop(current_index))

separator = ','
print(f'[{separator.join(executed_people)}]')








