numbers_of_string = int(input())
word = input()

strings = []
filtered_strings = []

for _ in range(numbers_of_string):
    current_string = input()
    strings.append(current_string)

print(strings)

for string in strings:
    if word in string:
        filtered_strings.append(string)

print(filtered_strings)
