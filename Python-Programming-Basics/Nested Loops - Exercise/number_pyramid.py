number = int(input())

number_counter = 0
flag = False

for row in range(1, number + 1):
    for col in range(row):
        number_counter += 1
        print(number_counter, end=" ")
        if number_counter == number:
            flag = True
            break
    print()
    if flag:
        break
