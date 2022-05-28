key = int(input())
characters_numbers = int(input())

string = ""

for character in range(characters_numbers):
    current_character = input()
    ord_of_character = ord(current_character) + key
    string += chr(ord_of_character)

print(string)
