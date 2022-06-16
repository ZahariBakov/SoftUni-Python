text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

new_text = [x for x in text if x not in vowels]

print("".join(new_text))
