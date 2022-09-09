original_string = input()

s = []

for char in original_string:
    s.append(char)

reversed_string = ''

while s:
    reversed_string += s.pop()

print(reversed_string)