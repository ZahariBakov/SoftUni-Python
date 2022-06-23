targets = list(map(int, input().split()))
shot_targets = 0
command = input()

while command != "End":
    index = int(command)
    if 0 <= index < len(targets):
        if targets[index] != -1:
            shot_targets += 1
            current_power = targets[index]
            targets[index] = -1
            for i in range(len(targets)):
                if targets[i] != -1:
                    if targets[i] <= current_power:
                        targets[i] += current_power
                    else:
                        targets[i] -= current_power
    command = input()

string_targets = " ".join([str(x) for x in targets])
print(f"Shot targets: {shot_targets} -> {string_targets}")
