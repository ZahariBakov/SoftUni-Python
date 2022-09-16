numbers = list(map(int, input().split()))
target = int(input())

while numbers:
    i = 0
    first = numbers.pop(0)

    while i < len(numbers):
        second = numbers[i]

        if first + second == target:
            print(f"{first} + {second} = {target}")
            if i + 1 >= len(numbers):
                break
            else:
                first = numbers[i + 1]
                numbers.pop(i)

        i += 1
