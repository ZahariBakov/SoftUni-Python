rows, cols = (int(x) for x in input().split())
matrix = [input().split() for _ in range(rows)]

command = input()

while command != "END":
    valid = True
    if command.startswith("swap"):
        command = command.split()
        if len(command) == 5:
            if 0 <= int(command[1]) < rows \
                    and 0 <= int(command[2]) < cols \
                    and 0 <= int(command[3]) < rows \
                    and 0 <= int(command[4]) < cols:
                second = (matrix[int(command[3])][int(command[4])])
                matrix[int(command[3])][int(command[4])] = matrix[int(command[1])][int(command[2])]
                matrix[int(command[1])][int(command[2])] = second
                for row in range(rows):
                    print(" ".join(matrix[row]))
            else:
                valid = False
        else:
            valid = False

    else:
        valid = False

    if not valid:
        print("Invalid input!")

    command = input()
