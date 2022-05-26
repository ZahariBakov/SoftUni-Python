string = input()

capital_letters = []

for index, digit in enumerate(string):
    if digit.isupper():
        capital_letters.append(index)

print(capital_letters)
