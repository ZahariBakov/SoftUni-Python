import re

text = input()
word = input()

search_pattern = fr'\b{word}\b'
match = re.findall(search_pattern, text, re.I)

print(len(match))
