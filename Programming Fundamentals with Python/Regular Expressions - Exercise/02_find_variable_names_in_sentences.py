import re

pattern = r'\b_([a-z]*)\b'
text = input()
result = []

matches = re.finditer(pattern, text, re.IGNORECASE)

for match in matches:
    if match:
        result.append(match.group(1))

print(','.join(result))
