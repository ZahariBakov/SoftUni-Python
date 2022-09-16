number_of_lines = int(input())
max_length = [0, []]

for _ in range(number_of_lines):
    intersection = []
    first, second = input().split("-")
    first_start = int(first.split(",")[0])
    first_end = int(first.split(",")[1])
    second_start = int(second.split(",")[0])
    second_end = int(second.split(",")[1])

    start = max(first_start, second_start)
    end = min(first_end, second_end)

    for num in range(start, end + 1):
        intersection.append(num)

    length = len(intersection)

    if max_length[0] < length:
        max_length[0] = length
        max_length[1] = intersection

print(f"Longest intersection is {max_length[1]} with length {max_length[0]}")
