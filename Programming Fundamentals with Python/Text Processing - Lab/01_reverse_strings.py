def reverse_text(text):
    reversed_text = text[::-1]
    print(f"{text} = {reversed_text}")


while True:
    command = input()

    if command == "end":
        break

    reverse_text(command)
