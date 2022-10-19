size = 7

dartboard = []
first_player_score, second_player_score = 501, 501
first_player_name, second_player_name = input().split(', ')
first_player_throws = 0
second_player_throws = 0
win = ''

for row in range(size):
    col = input().split()
    dartboard.append(col)

while first_player_score > 0 or second_player_score > 0:
    # first player turn
    row, col = eval(input())
    first_player_throws += 1
    if 0 <= row < size and 0 <= col < size:
        if dartboard[row][col] == "B":
            win = "first"
            break
        elif dartboard[row][col] == "D":
            first_player_score -= (int(dartboard[0][col]) + int(dartboard[6][col]) +
                                   int(dartboard[row][0]) + int(dartboard[row][6])) * 2
        elif dartboard[row][col] == "T":
            first_player_score -= (int(dartboard[0][col]) + int(dartboard[6][col]) +
                                   int(dartboard[row][0]) + int(dartboard[row][6])) * 3
    if first_player_score < 1:
        win = "first"
        break

    # second player turn
    row, col = eval(input())
    second_player_throws += 1
    if 0 <= row < size and 0 <= col < size:
        if dartboard[row][col] == "B":
            win = "second"
            break
        elif dartboard[row][col] == "D":
            second_player_score -= (int(dartboard[0][col]) + int(dartboard[6][col]) +
                                   int(dartboard[row][0]) + int(dartboard[row][6])) * 2
        elif dartboard[row][col] == "T":
            second_player_score -= (int(dartboard[0][col]) + int(dartboard[6][col]) +
                                   int(dartboard[row][0]) + int(dartboard[row][6])) * 3

    if second_player_score < 1:
        win = "second"
        break

if win == "first":
    print(f"{first_player_name} won the game with {first_player_throws} throws!")
else:
    print(f"{second_player_name} won the game with {second_player_throws} throws!")
