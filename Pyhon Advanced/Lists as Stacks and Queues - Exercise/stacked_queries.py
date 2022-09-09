stack = []
lines = int(input())
final_result = ""

for _ in range(lines):
    command = input()

    if command.startswith("1"):
        current_number = int(command.split(" ")[1])
        stack.append(current_number)

    elif command.startswith("2"):
        if stack:
            stack.pop()

    elif command.startswith("3"):
        print(max(stack))

    elif command.startswith("4"):
        print(min(stack))

if stack:
    while stack:
        final_result += str(stack.pop()) + ", "

print(final_result[:-2])

