string = input()
stack = []
pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}
balanced = True

for ch in string:

    if ch in "([{":
        stack.append(ch)

    elif not stack:
            balanced = False

    else:
        opening_bracket = stack.pop()

        if pairs[opening_bracket] != ch:
            balanced = False

    if not balanced:
        break

if not balanced or stack:
    print("NO")

else:
    print("YES")
