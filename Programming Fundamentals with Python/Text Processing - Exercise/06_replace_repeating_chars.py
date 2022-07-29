string = input()
text = string[0]

last_character = string[0]

for i in range(1, len(string)):
    if string[i] != last_character:
        text += string[i]
        last_character = string[i]

print(text)
