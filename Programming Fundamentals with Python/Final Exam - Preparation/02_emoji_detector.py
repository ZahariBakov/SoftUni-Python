import re

cool_sum = 1
text = input()
digit_pattern = r'\d'
emojis_pattern = r'\:{2}[A-Z][a-z]{2,}\:{2}|\*{2}[A-Z][a-z]{2,}\*{2}'

all_digits = re.findall(digit_pattern, text)
valid_emojis = re.findall(emojis_pattern, text)
for digit in all_digits:
    cool_sum *= int(digit)
print(cool_sum)

for match in valid_emojis:
    current_sum = 0
    for char in match:
        current_sum += ord(char)
    if current_sum > cool_sum:
        print(match)



