def square(r, c):
    r = str(abs(r - 8))
    c = chr(c + 97)
    return c + r


size = 8
board = []
white = []
black = []

for row in range(size):
    col = input().split()
    if 'w' in col:
        white = [row, col.index('w')]
    if 'b' in col:
        black = [row, col.index('b')]
    board.append(col)

while True:
    # white turn
    row, col = white
    if col != 0:
        if board[row - 1][col - 1] == 'b':
            square = square(row - 1, col - 1)
            print(f"Game over! White win, capture on {square}.")
            break
    if col != 7:
        if board[row - 1][col + 1] == 'b':
            square = square(row - 1, col + 1)
            print(f"Game over! White win, capture on {square}.")
            break

    white = row - 1, col
    board[white[0]][white[1]] = 'w'
    if white[0] == 0:
        square = square(white[0], white[1])
        print(f"Game over! White pawn is promoted to a queen at {square}.")
        break

    # black turn
    row, col = black
    if col != 0:
        if board[row + 1][col - 1] == 'w':
            square = square(row + 1, col - 1)
            print(f"Game over! Black win, capture on {square}.")
            break
    if col != 7:
        if board[row + 1][col + 1] == 'w':
            square = square(row + 1, col + 1)
            print(f"Game over! Black win, capture on {square}.")
            break

    black = row + 1, col
    board[black[0]][black[1]] = 'b'
    if black[0] == 7:
        square = square(black[0], black[1])
        print(f"Game over! Black pawn is promoted to a queen at {square}.")
        break


