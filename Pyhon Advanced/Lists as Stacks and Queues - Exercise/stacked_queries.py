stack = []
lines = int(input())
final_result = []

for _ in range(lines):
    command = input().split()

    if command[0] == "1":
        current_number = int(command[1])
        stack.append(current_number)

    elif command[0] == "2" and stack:
        stack.pop()

    elif command[0] == "3" and stack:
        print(max(stack))

    elif command[0] == "4" and stack:
        print(min(stack))

if stack:
    while stack:
        final_result.append(str(stack.pop()))

print(", ".join(final_result))
