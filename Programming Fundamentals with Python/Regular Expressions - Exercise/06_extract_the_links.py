import re

pattern = r'(w{3}\.[A-Za-z0-9]+(\-[A-z0-9]+)*(\.[a-z]+)+)'
text = input()

while True:
    if text:
        match = re.search(pattern, text)
        if match:
            print(match.group(1))
    else:
        break
    text = input()
