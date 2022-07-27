import re

text = input()
word = input()

search_pattern = fr'\b{word}\b'
matches = re.findall(search_pattern, text, re.I)

print(len(matches))

