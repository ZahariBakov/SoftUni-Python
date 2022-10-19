size = 6

board = []
points = 0

for row in range(size):
    col = input().split()
    board.append(col)

for _ in range(3):
    row, col = eval(input())
    if 0 <= row < size and 0 <= col < size:
        if board[row][col] == 'B':
            board[row][col] = 0
            for num in range(size):
                if board[num][col] != "B":
                    points += int(board[num][col])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    if points < 200:
        prize = "Football"
    elif points < 300:
        prize = "Teddy Bear"
    else:
        prize = "Lego Construction Set"

    print(f"Good job! You scored {points} points, and you've won {prize}.")
