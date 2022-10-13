def directions(way, r, c):
    if way == "up":
        r -= 1
    elif way == "down":
        r += 1
    elif way == "left":
        c -= 1
    elif way == "right":
        c += 1

    return r, c


size = 6
matrix = [[x for x in input().split()] for _ in range(size)]

row, col = eval(input())
empty_position = "."

command = input()

while command != "Stop":
    command_name = command.split(", ")[0]
    direction = command.split(", ")[1]

    if command_name == "Create":
        value = command.split(", ")[2]
        row, col = directions(direction, row, col)
        if matrix[row][col] == empty_position:
            matrix[row][col] = value
    elif command_name == "Update":
        value = command.split(", ")[2]
        row, col = directions(direction, row, col)
        if matrix[row][col] != empty_position:
            matrix[row][col] = value
    elif command_name == "Delete":
        row, col = directions(direction, row, col)
        if matrix[row][col] != empty_position:
            matrix[row][col] = empty_position
    elif command_name == "Read":
        row, col = directions(direction, row, col)
        if matrix[row][col] != empty_position:
            print(matrix[row][col])

    command = input()

for el in matrix:
    print(" ".join(el))
