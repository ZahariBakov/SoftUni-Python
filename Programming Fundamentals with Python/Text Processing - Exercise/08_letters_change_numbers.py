words = input().split()

total_sum = 0

for word in words:
    current_sum = 0
    first_num = (ord(word[0].upper()) - 64)
    second_num = (ord(word[-1].upper()) - 64)
    current_number = int(word[1:-1])

    if word[0].isupper():
        current_sum = current_number / first_num

    elif word[0].islower():
        current_sum = current_number * first_num

    if word[-1].isupper():
        current_sum -= second_num

    elif word[-1].islower():
        current_sum += second_num

    total_sum += current_sum

print(f"{total_sum:.2f}")
