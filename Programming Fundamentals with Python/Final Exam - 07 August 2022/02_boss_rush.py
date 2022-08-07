import re

pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#'

number_of_enters = int(input())

for _ in range(number_of_enters):
    text = input()
    access_denied = False
    matches = re.finditer(pattern, text)

    for match in matches:
        access_denied = True
        print(f"{match.group(1)}, The {match.group(2)}")
        print(f">> Strength: {len(match.group(1))}\n>> Armor: {len(match.group(2))}")

    if not access_denied:
        print("Access denied!")
