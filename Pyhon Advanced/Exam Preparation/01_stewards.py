from collections import deque

seats = input().split(", ")
first_sequence = deque([int(x) for x in input().split(", ")])
second_sequence = [int(x) for x in input().split(", ")]
rotation = 0
matches =[]

while True:
    first_num = first_sequence.popleft()
    second_num = second_sequence.pop()
    character = chr(first_num + second_num)
    rotation += 1

    first_match = str(first_num) + character
    second_match = str(second_num) + character

    if first_match in matches or second_match in matches:
        continue
    elif first_match in seats:
        matches.append(first_match)

    elif second_match in seats:
        matches.append(second_match)

    else:
        first_sequence.append(first_num)
        second_sequence.insert(0, second_num)

    if len(matches) == 3:
        break

    if rotation == 10:
        break

print(f"Seat matches: {', '.join(matches)}")
print(f"Rotations count: {rotation}")
