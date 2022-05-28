number = int(input())

for first_number in range(97, 97 + number):
    for second_number in range(97, 97 + number):
        for third_number in range(97, 97 + number):
            print(f"{chr(first_number)}{chr(second_number)}{chr(third_number)}")
