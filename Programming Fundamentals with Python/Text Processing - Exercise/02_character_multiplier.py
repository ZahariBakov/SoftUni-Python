def shorter_text(long, short, sum_of_characters):
    for short_index in range(len(short)):
        sum_of_characters += ord(long[short_index]) * ord(short[short_index])

    for long_index in range(short_index + 1, len(long)):
        sum_of_characters += ord(long[long_index])

    return sum_of_characters


first, second = input().split(" ")
total_sum = 0

if len(first) > len(second):
    print(shorter_text(first, second, total_sum))

elif len(first) < len(second):
    print(shorter_text(second, first, total_sum))

else:
    for i in range(len(first)):
        total_sum += ord(first[i]) * ord(second[i])
    print(total_sum)
