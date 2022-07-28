import re

text = input()
pattern = r'([\d])|(\*{2}[A-Z][a-z]{2,}\*{2})|(:{2}[A-Z][a-z]{2,}:{2})'
cool_threshold = 1
elements = {}

matches = re.finditer(pattern, text)

for match in matches:
    current_element = match.group()

    if current_element.isdigit():
        cool_threshold *= int(current_element)

    else:
        elements[current_element] = 0

        for char in current_element:
            if char != "*" and char != ":":
                elements[current_element] += ord(char)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(elements)} emojis found in the text. The cool ones are:")
for word in elements:
    if elements[word] >= cool_threshold:
        print(word)
