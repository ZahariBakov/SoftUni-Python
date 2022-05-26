number = int(input())

for num in range(1, number + 1):
    special = False
    if num == 5 or num == 7:
        special = True
    elif num > 11:
        sum_of_num = 0
        string_num = str(num)
        for i in string_num:
            sum_of_num += int(i)
            if sum_of_num == 5 or sum_of_num == 7 or sum_of_num == 11:
                special = True

    if special:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
