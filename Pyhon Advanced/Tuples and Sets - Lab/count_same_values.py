numbers = ([float(x) for x in input().split()])
dictionary = {}

for num in numbers:
    if num not in dictionary:
        dictionary[num] = 0

    dictionary[num] += 1

for data in dictionary.items():
    print(f"{data[0]} - {data[1]} times")
