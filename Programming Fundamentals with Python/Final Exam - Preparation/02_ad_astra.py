import re

string = input()

pattern = r'([|#])([A-Za-z\s]+)\1([\d]{2}\/[0\d]{2}\/[\d]{2})\1([\d]+)\1'
matches = re.finditer(pattern, string)

foods = []
calorie = 0

for match in matches:
    foods.append({"food": match.group(2), "date": match.group(3), "calc": match.group(4)})
    calorie += int(match.group(4))

days = calorie // 2000
print(f"You have food to last you for: {days} days!")

for item in foods:
    print(f"Item: {item['food']}, Best before: {item['date']}, Nutrition: {item['calc']}")
