first_character = input()
second_character = input()


def characters_in_range(a, b):
    first_int = ord(a)
    second_int = ord(b)
    final_text = ""
    for number in range(first_int + 1, second_int):
        current_character = chr(number)
        final_text += current_character + " "
    return final_text


print(characters_in_range(first_character, second_character))
