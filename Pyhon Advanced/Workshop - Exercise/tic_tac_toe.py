class NonValidNumber(Exception):
    pass


def verify_number(num, positions):
    if num not in positions:
        raise NonValidNumber


def creating_players():
    first_player_name = input("Player one name: ")
    second_player_name = input("Player two name: ")

    first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? ").upper()
    while first_player_sign not in ['X', 'O']:
        first_player_sign = input(f"{first_player_name} would you like to play with 'X' or 'O'? ").upper()

    second_player_sign = 'O' if first_player_sign == 'X' else 'X'

    return [(first_player_name, first_player_sign), (second_player_name, second_player_sign)]


def print_board_numerical(matrix, size):
    print("This is the numerical of the board:")
    number = 1
    for row in range(size):
        print("|", end='')
        for col in range(size):
            if number >= 10:
                print(f"  {number} |", end='')
            else:
                print(f"  {number}  |", end='')
            number += 1
        print()


def get_position_mapping(matrix, size):
    result = {}
    key = 1
    for row in range(size):
        for col in range(size):
            result[key] = (row, col)
            key += 1
    return result


def print_board(matrix):
    for row in range(len(matrix)):
        print("|", end='')
        for col in range(len(matrix)):
            print(f"  {' ' if matrix[row][col] is None else board[row][col]}  |", end='')
        print()
    return matrix


def check_for_winner(ma, sign, r, c, size):
    row_won = True
    for col in range(size):
        if ma[r][col] != sign:
            row_won = False
            break
    if row_won:
        return True

    col_won = True
    for row in range(size):
        if ma[row][c] != sign:
            col_won = False
            break
    if col_won:
        return True
    primary_won = True
    for idx in range(size):
        if board[idx][idx] != sign:
            primary_won = False
            break
    if primary_won:
        return True
    secondary_won = True
    for idx in range(size):
        if board[idx][size - 1 - idx] != sign:
            secondary_won = False
            break
    return secondary_won


def check_for_draw(ma, size):
    for row in range(size):
        for col in range(size):
            if ma[row][col] is None:
                return False
    return True


def play_game(players, matrix, position):
    while True:
        player_name, player_sign = players[0]
        try:
            current_position = int(input(f"{player_name} choose a free position [1-9]: "))
            verify_number(current_position, position)

        except NonValidNumber:
            print("This number not valid, please enter a valid number!")
        except ValueError:
            print("Please select a valid digit!")
            continue

        row, col = position[current_position]

        if matrix[row][col] is not None:
            print("Sorry, this position has already been chosen. Please select another position.")
            continue

        matrix[row][col] = player_sign
        matrix = print_board(matrix)

        if check_for_winner(matrix, player_sign, row, col, board_size):
            print(f"{player_name} won!")
            break

        if check_for_draw(matrix, board_size):
            print('Draw!')
            break

        players[0], players[1] = players[1], players[0]


players = creating_players()

board_size = 3
board = [([None] * board_size) for _ in range(board_size)]

print_board_numerical(board, board_size)
print(f"{players[0][0]} starts first!")

position_mapping = get_position_mapping(board, board_size)
play_game(players, board, position_mapping)

while True:
    new_game_choice = input("Do you want play another game? [y/n]: ")

    if new_game_choice == 'y':
        print_board_numerical(board, board_size)
        board = [([None] * board_size) for _ in range(board_size)]
        print(f"{players[0][0]} starts first!")
        play_game(players, board, position_mapping)
    else:
        print("See you again!")
        break

