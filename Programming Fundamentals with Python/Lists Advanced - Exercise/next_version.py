old_version = list(map(int, input().split(".")))

if old_version[-1] == 9:
    old_version[-1] = 0
    if old_version[1] == 9:
        old_version[1] = 0
        old_version[0] += 1
    else:
        old_version[1] += 1
else:
    old_version[-1] += 1

new_version = [str(x) for x in old_version]
print(".".join(new_version))
