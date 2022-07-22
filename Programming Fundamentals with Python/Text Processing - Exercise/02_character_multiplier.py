def shorter_text(long, short, sum):
    for i in range(len(short)):
        sum += ord(long[i]) * ord(short[i])

    for j in range(i + 1, len(long)):
        sum += ord(long[j])

    return sum


first, second = input().split(" ")
sum = 0

if len(first) > len(second):
    print(shorter_text(first, second, sum))

elif len(first) < len(second):
    print(shorter_text(second, first, sum))

else:
    for i in range(len(first)):
        sum += ord(first[i]) * ord(second[i])
    print(sum)
