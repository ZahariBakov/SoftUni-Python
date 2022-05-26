number = int(input())

first_num = 0
second_num = 0
third_num = 0
fourth_num = 0
for i in range(1, 10):
    if number % i == 0:
        first_num = i
        for j in range(1, 10):
            if number % j == 0:
                second_num = j
                for y in range(1, 10):
                    if number % y == 0:
                        third_num = y
                        for k in range(1, 10):
                            if number % k == 0:
                                fourth_num = k
                                print(f"{first_num}{second_num}{third_num}{fourth_num}", end=" ")
