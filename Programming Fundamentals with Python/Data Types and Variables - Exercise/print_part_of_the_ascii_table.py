start_character = int(input())
final_character = int(input())

string = ""

for letter in range(start_character, final_character + 1):
    string += chr(letter) + " "

print(string)
