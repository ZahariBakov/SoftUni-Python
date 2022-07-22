text = input()
new_text = ""

for character in text:
    ord_char = ord(character) + 3
    new_text += chr(ord_char)

print(new_text)
