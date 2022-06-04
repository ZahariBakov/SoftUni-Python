factor = int(input())
count = int(input())

list_of_number = []
current_number = 0

for num in range(count):
    new_number = current_number + factor
    list_of_number.append(new_number)
    current_number = new_number

print(list_of_number)
