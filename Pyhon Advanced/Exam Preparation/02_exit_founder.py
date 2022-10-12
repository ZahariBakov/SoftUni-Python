first_player, second_player = input().split(', ')

board = []

for _ in range(6):
    board.append(input().split())

first_player_rest = False
second_player_rest = False

while True:
    first_player_coordinates = input()
    if not first_player_rest:
        row, col = map(int, first_player_coordinates.strip("(").strip(")").split(", "))
        current_position = board[row][col]

        if current_position == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        if current_position == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_rest = True
        if current_position == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
    else:
        first_player_rest = False

    second_player_coordinates = input()
    if not second_player_rest:
        row, col = map(int, second_player_coordinates.strip("(").strip(")").split(", "))
        current_position = board[row][col]

        if current_position == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        if current_position == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_rest = True
        if current_position == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
    else:
        second_player_rest = False
