import re

some_string = input()
pattern = r'=[A-Z][A-Za-z]{2,}=|\/[A-Z][A-Za-z]{2,}\/'
matches = re.findall(pattern, some_string)
destinations = []
travel_points = 0

for match in matches:
    match = ''.join([match[i] for i in range(len(match)) if 0 < i < (len(match) - 1)])
    destinations.append(match)
    travel_points += len(match)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
