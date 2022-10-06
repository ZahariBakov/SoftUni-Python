class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


# Print matrix
def print_matrix(mrx):
    for el in mrx:
        print(el)


# Verify player choice of column number of the column - if not, ask again
def verify_column_choice(col, max_col_idx):
    if not (0 <= col <= max_col_idx):
        raise InvalidColumnError


# Place player marker on the spot
# Check if the column is full if so - throw error.
def place_player_choice(ma, selected_column_idx, player):
    rows = len(ma) - 1
    for row_idx in range(rows, -1, -1):
        if ma[row_idx][selected_column_idx] == 0:
            ma[row_idx][selected_column_idx] = player
            return row_idx, selected_column_idx
    raise FullColumnError


def is_horizontal(matrix, row, col, player, count):
    """
    We check for both sides, because we can input like this:
    1
    1
    2
    2
    4
    4
    3
    If we do not check for both there will be winner, but we can not now that.
    Also we check for this condition:
    1
    1
    2
    2
    5
    5
    6
    6
    7
    7
    3
    [True, True, True, False, True, True, True] - This is not a winner!
    """
    right = []
    for idx in range(count):
        if check_index(matrix, row, col + idx, player):
            right.append(True)
        else:
            break
    left = []
    for idx in range(count):
        if check_index(matrix, row, col - idx, player):
            left.append(True)
        else:
            break
    # right_count = [check_index(matrix, row, col + idx, player) for idx in range(count - 1)].count(True)
    # left_count = [check_index(matrix, row, col - idx, player) for idx in range(count - 1)].count(True)
    # it should be strict '>' because we are counting the current element as well.
    return len(right + left) > count


def is_right_diagonal(matrix, row, col, player, count):
    """
    We check for both sides (up right and down left diagonals) so we can look for the same problem -
    adding element which is not only to one side with 4, but for both.
    """
    right_up = []
    for idx in range(count):
        if check_index(matrix, row - idx, col + idx, player):
            right_up.append(True)
        else:
            break
    left_down = []
    for idx in range(count):
        if check_index(matrix, row + idx, col - idx, player):
            left_down.append(True)
        else:
            break
    # right_up_count = [check_index(matrix, row - idx, col + idx, player) for idx in range(count - 1)].count(True)
    # left_down_count = [check_index(matrix, row + idx, col - idx, player) for idx in range(count - 1)].count(True)
    return len(right_up + left_down) > count


def is_left_diagonal(matrix, row, col, player, count):
    """
    We check for both sides (up left and down right diagonals) so we can look for the same problem -
    adding element which is not only to one side with 4, but for both.
    """
    right_down = []
    for idx in range(count):
        if check_index(matrix, row + idx, col + idx, player):
            right_down.append(True)
        else:
            break
    left_up = []
    for idx in range(count):
        if check_index(matrix, row - idx, col - idx, player):
            left_up.append(True)
        else:
            break
    # left_up_count = [check_index(matrix, row-idx, col-idx, player) for idx in range(count - 1)].count(True)
    # right_down_count = [check_index(matrix, row + idx, col + idx, player) for idx in range(count - 1)].count(True)
    return len(right_down + left_up) > count


# Define winning conditions.
def is_winner(matrix, row, col, player, count=4):
    """
    We check for horizontal (both sides)
    Only down (because we fill the matrix from bottom to top.)
    Check for left and right diagonal.
    """
    is_right = all([check_index(matrix, row, col + idx, player) for idx in range(count)])
    is_left = all([check_index(matrix, row, col - idx, player) for idx in range(count)])
    is_down = all([check_index(matrix, row + idx, col, player) for idx in range(count)])
    is_left_up = all([check_index(matrix, row - idx, col - idx, player) for idx in range(count)])
    is_right_up = all([check_index(matrix, row - idx, col + idx, player) for idx in range(count)])
    is_left_down = all([check_index(matrix, row + idx, col - idx, player) for idx in range(count)])
    is_right_down = all([check_index(matrix, row + idx, col + idx, player) for idx in range(count)])

    if any([  # is_right,
        # is_left,
        is_down,
        # is_left_up,
        # is_right_up,
        # is_left_down,
        # is_right_down,
        is_horizontal(matrix, row, col, player, count),
        is_right_diagonal(matrix, row, col, player, count),
        is_left_diagonal(matrix, row, col, player, count)]):
        return True
    return False


# Check indexes.
def check_index(matrix, row, col, player):
    if col < 0 or row < 0:
        return False
    try:
        if matrix[row][col] == player:
            return True
    except IndexError:
        return False
    return False


# Create matrix
rows_count = 6
cols_count = 7
board = [[0 for col in range(cols_count)] for row in range(rows_count)]

print('Wellcome to the game "Four connect"!')

first_player_name = input("Enter First player Name: ")
second_player_name = input("Enter Second player Name: ")

# Print initial board
print("This is game board")
print_matrix(board)

player_num = 1
while True:
    try:
        # Read column choice from input
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        verify_column_choice(column_num, cols_count - 1)
        row, col = place_player_choice(board, column_num, player_num)
        print_matrix(board)
        if is_winner(board, row, col, player_num):
            if player_num == 1:
                print(f"The winner is player {first_player_name}!!!")
            else:
                print(f"The winner is player {second_player_name}!!!")
            break

    except ValueError:
        # Not a valid number.
        print("Please select a valid digit!")
        continue
    except InvalidColumnError:
        # Not in range of the board.
        print(f"This column is not valid. Please select a number between 1 and {cols_count}: ")
        continue
    except FullColumnError:
        # This is already a full column.
        print(f"This column is already full! Please select other column number!")
        continue

    # Decide correct players num (only 2 possible). Only if the turn was successful we go to the next player.
    if player_num == 1:
        player_num += 1
    else:
        player_num -= 1