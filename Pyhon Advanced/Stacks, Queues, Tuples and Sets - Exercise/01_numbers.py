first = {int(x) for x in input().split()}
second = {int(x) for x in input().split()}
lines = int(input())

for _ in range(lines):
    commands_parts = input().split()

    if commands_parts[0] == "Add":
        if commands_parts[1] == "First":
            first = first.union([int(x) for x in commands_parts[2:]])

        else:
            second = second.union([int(x) for x in commands_parts[2:]])

    elif commands_parts[0] == "Remove":
        if commands_parts[1] == "First":
            first = first.difference([int(x) for x in commands_parts[2:]])

        else:
            second = second.difference([int(x) for x in commands_parts[2:]])

    elif commands_parts[0] == "Check":
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
