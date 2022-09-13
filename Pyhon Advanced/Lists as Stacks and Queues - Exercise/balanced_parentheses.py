string = input()
stack = []
balanced = True

for ch in string:
    if not balanced:
        break

    if ch == "(" or ch == "[" or ch == "{":
        stack.append(ch)

    else:
        if not stack:
            balanced = False
            break
        else:
            if ch == ")":
                if stack.pop() != "(":
                    balanced = False
                    break

            elif ch == "]":
                if stack.pop() != "[":
                    balanced = False
                    break

            elif ch == "}":
                if stack.pop() != "{":
                    balanced = False
                    break

if balanced:
    print("YES")

else:
    print("NO")
