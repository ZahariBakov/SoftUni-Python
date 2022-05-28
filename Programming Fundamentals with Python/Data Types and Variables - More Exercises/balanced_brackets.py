character_lines = int(input())

opening_bracket = False
closing_bracket = False
opening = 0
closing = 0

for i in range(character_lines):
    current_sting = input()
    if current_sting == "(":
        if not opening_bracket:
            opening_bracket = True
            opening += 1
            if closing_bracket:
                closing_bracket = False
        else:
            opening += 1
            break
    if current_sting == ")":
        if not closing_bracket:
            closing_bracket = True
            closing += 1
            if opening_bracket:
                opening_bracket = False
        else:
            closing += 1
            break

if opening == closing:
    print("BALANCED")
else:
    print("UNBALANCED")
