searched = input()
text = input()

while searched in text:
    text = text.replace(searched, "")

print(text)
