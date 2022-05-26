number = input()

sorted_number = sorted(number, reverse=True)

for i in range(len(number)):
    print(sorted_number[i], end="")
