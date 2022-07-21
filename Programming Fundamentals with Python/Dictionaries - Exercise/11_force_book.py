users_dictionary = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")

    elif "->" in command:
        user, side = command.split(" -> ")
        for key, value in users_dictionary.items():
            if user in value:
                users_dictionary[key].remove(user)

    if side not in users_dictionary:
        users_dictionary[side] = []

    found = False
    for value in users_dictionary.values():
        if user in value:
            found = True
            break
    if not found:
        users_dictionary[side].append(user)
        if "->" in command:
            print(f"{user} joins the {side} side!")

for side in users_dictionary:
    if len(users_dictionary[side]) > 0:
        print(f"Side: {side}, Members: {len(users_dictionary[side])}")
        [print(f"! {force_user}") for force_user in users_dictionary[side]]

