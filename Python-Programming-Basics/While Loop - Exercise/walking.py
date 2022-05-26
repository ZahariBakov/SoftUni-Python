command = input()

step = 0
reached = False

while command != "Going home":
    step += int(command)
    if step >= 10000:
        reached = True
        break
    command = input()

if reached:
    print("Goal reached! Good job!")
    print(f"{step - 10000} steps over the goal!")
else:
    command = int(input())
    step += command
    if step >= 10000:
        print("Goal reached! Good job!")
        print(f"{step - 10000} steps over the goal!")
    else:
        print(f"{10000 - step} more steps to reach goal.")
