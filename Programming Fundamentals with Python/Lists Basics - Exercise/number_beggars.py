list_of_integer = input().split(", ")
beggars = [0] * int(input())
index = 0

for number in list_of_integer:
    current_number = int(number)
    beggars[index] += current_number
    index += 1
    if index == len(beggars):
        index = 0

print(beggars)
