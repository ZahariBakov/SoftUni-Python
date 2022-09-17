lines = int(input())
odd_set = set()
even_set = set()

for row in range(1, lines + 1):
    name = input()
    current_sum = 0

    for ch in name:
        current_sum += ord(ch)

    current_result = int(current_sum / row)

    if current_result % 2 == 0:
        even_set.add(current_result)

    else:
        odd_set.add(current_result)

if sum(even_set) == sum(odd_set):
    result = odd_set.union(even_set)

elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)

else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")
