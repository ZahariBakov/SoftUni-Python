width = int(input())
length = int(input())

pieces = width * length
command = input()

while command != "STOP":
    pieces -= int(command)
    if pieces < 0:
        break
    command = input()

if pieces < 0:
    print(f"No more cake left! You need {abs(pieces)} pieces more.")
else:
    print(f"{pieces} pieces are left.")
