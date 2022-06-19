secret_message = input().split()
final_message = []

for word in secret_message:
    digit_at_string = ""
    characters_list = []
    for character in word:
        if character.isdigit():
            digit_at_string += character
        else:
            characters_list.append(character)
    digit = int(digit_at_string)
    convert_digit = chr(digit)
    temporary_first = characters_list[0]
    temporary_last = characters_list[-1]
    characters_list.pop(0)
    characters_list.insert(0, temporary_last)
    characters_list.pop()
    characters_list.append(temporary_first)
    convert_digit += "".join(characters_list)
    final_message.append(convert_digit)

print(" ".join(final_message))
