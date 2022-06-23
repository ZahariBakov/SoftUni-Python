sequence_of_elements = input().split()
player_turn = input()
turns = 1

while player_turn != "end":
    current_turn = player_turn.split()
    first_position = int(current_turn[0])
    second_position = int(current_turn[1])
    if first_position == second_position or first_position < 0 or second_position < 0 or first_position >= len(sequence_of_elements) or second_position >= len(sequence_of_elements):
        print("Invalid input! Adding additional elements to the board")
        len_of_sequence = len(sequence_of_elements) // 2
        sequence_of_elements.insert(len_of_sequence, f"-{turns}a")
        sequence_of_elements.insert(len_of_sequence, f"-{turns}a")
    elif sequence_of_elements[first_position] == sequence_of_elements[second_position]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_position]}!")
        remove_elements = sequence_of_elements[first_position]
        sequence_of_elements.remove(remove_elements)
        sequence_of_elements.remove(remove_elements)
    else:
        print("Try again!")
    if len(sequence_of_elements) == 0:
        print(f"You have won in {turns} turns!")
        break
    turns += 1
    player_turn = input()

if player_turn == "end":
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
