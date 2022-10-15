from collections import deque


def movement(n, idx):
    if idx < 0:
        idx = n - 1
    elif idx == n:
        idx = 0

    return idx


size = 6
land = []
water = False
concrete = False
metal = False

for r in range(size):
    c = input().split()
    land.append(c)
    if "E" in c:
        row, col = r, c.index("E")
        land[row][col] = "-"

commands = deque(input().split(", "))

while commands:
    current_command = commands.popleft()

    if current_command == "up":
        row = movement(size, row - 1)
    elif current_command == "down":
        row = movement(size, row + 1)
    elif current_command == "left":
        col = movement(size, col - 1)
    elif current_command == "right":
        col = movement(size, col + 1)

    if land[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break
    elif land[row][col] == "W":
        print(f"Water deposit found at ({row}, {col})")
        water = True
    elif land[row][col] == "C":
        print(f"Concrete deposit found at ({row}, {col})")
        concrete = True
    elif land[row][col] == "M":
        print(f"Metal deposit found at ({row}, {col})")
        metal = True

if water and concrete and metal:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
