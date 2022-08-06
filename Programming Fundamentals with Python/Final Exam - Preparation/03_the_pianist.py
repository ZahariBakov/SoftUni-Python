def add(dict, piece, composer, key):
    if piece in dict:
        print(f"{piece} is already in the collection!")

    else:
        dict[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")

    return dict


def remove(dict, piece):
    if piece in dict:
        del dict[piece]
        print(f"Successfully removed {piece}!")

    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")

    return dict


def change_key(dict, piece, key):
    if piece in dict:
        dict[piece]['key'] = key
        print(f"Changed the key of {piece} to {key}!")

    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


number_of_pieces = int(input())
pieces = {}

for _ in range(number_of_pieces):
    current_piece = input().split("|")
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    pieces[piece] = {'composer': composer, 'key': key}

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split("|")
    piece = command[1]

    if "Add" in command:
        composer = command[2]
        key = command[3]
        add(pieces, piece, composer, key)

    elif "Remove" in command:
        remove(pieces, piece)

    elif "ChangeKey" in command:
        key = command[2]
        change_key(pieces, piece, key)

for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")
