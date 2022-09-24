size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":
    type_command, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if row < 0 or row >= size or col < 0 or col >= size:
        print("Invalid coordinates")
    elif command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value

    command = input().split()

[print(*row) for row in matrix]
