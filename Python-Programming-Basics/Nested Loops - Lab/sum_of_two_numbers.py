start_num = int(input())
final_num = int(input())
magic_num = int(input())

combination = 0
found_magic = False

for i in range(start_num, final_num + 1):
    for j in range(start_num, final_num + 1):
        sum = i + j
        combination += 1
        if sum == magic_num:
            found_magic = True
            break

    if found_magic:
        break
if found_magic:
    print(f"Combination N:{combination} ({i} + {j} = {magic_num})")
else:
    print(f"{combination} combinations - neither equals {magic_num}")
