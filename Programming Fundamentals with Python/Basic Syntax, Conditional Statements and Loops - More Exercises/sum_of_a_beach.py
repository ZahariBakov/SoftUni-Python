text = input().lower()

my_list = ["sand", "water", "fish", "sun"]
counter = 0

for item in my_list:
    if item in text:
        counter += text.count(item)

print(counter)
