width = int(input())
length = int(input())
height = int(input())
boxes = input()

free_space = width * length * height

while boxes != "Done":
    free_space -= int(boxes)
    if free_space < 0:
        break
    boxes = input()

if free_space < 0:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
else:
    print(f"{free_space} Cubic meters left.")
