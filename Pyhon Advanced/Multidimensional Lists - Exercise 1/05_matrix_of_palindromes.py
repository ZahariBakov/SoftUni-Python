rows, cols = (int(x) for x in input().split())
matrix = []

for row in range(rows):
    submatrix = []
    for col in range(cols):
        current_col = chr(97 + row) + chr(97 + row + col) + chr(97 + row)
        submatrix.append(current_col)
    matrix.append(submatrix)

for row in range(rows):
    print(" ".join(matrix[row]))
