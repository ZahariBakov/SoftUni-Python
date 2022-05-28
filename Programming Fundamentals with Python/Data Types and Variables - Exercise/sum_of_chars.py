number_of_characters = int(input())
sum_of_character = 0

for letter in range(number_of_characters):
    current_character = input()
    sum_of_character += ord(current_character)

print(f"The sum equals: {sum_of_character}")
