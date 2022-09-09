expression = input()

parentheses = []

for i in range(len(expression)):
    char = expression[i]
    if char == "(":
        parentheses.append(i)

    elif char == ")":
        start_index = parentheses.pop()
        end_index = i + 1
        print(expression[start_index:end_index])

