text = input()
new_text = ''
explosion = 0

for i in range(len(text)):
    if text[i] == '>':
        explosion += int(text[i + 1])
        new_text += text[i]

    elif explosion > 0:
        explosion -= 1

    else:
        new_text += text[i]

print(new_text)
