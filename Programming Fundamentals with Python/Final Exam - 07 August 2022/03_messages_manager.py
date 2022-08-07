def add(dict, user, sent, received):
    if user not in dict:
        dict[user] = {"sent": sent, "received": received}

    return dict


def message(dict, sender, receiver):
    if sender in dict and receiver in dict:
        dict[sender]["sent"] += 1
        if dict[sender]["sent"] + dict[sender]["received"] >= capacity:
            del dict[sender]
            print(f"{sender} reached the capacity!")

        dict[receiver]["received"] += 1
        if dict[receiver]["received"] + dict[receiver]["sent"] >= capacity:
            del dict[receiver]
            print(f"{receiver} reached the capacity!")


def empty(dict, name):
    if name == "All":
        dict.clear()

    elif name in dict:
        del dict[name]

    return dict


capacity = int(input())
users = {}

while True:
    command = input()

    if command == "Statistics":
        break

    command = command.split("=")

    if "Add" in command:
        user_name = command[1]
        sent = int(command[2])
        received = int(command[3])
        add(users, user_name, sent, received)

    elif "Message" in command:
        sender = command[1]
        receiver = command[2]
        message(users, sender, receiver)

    elif "Empty" in command:
        user_name = command[1]
        empty(users, user_name)

print(f"Users count: {len(users)}")
for user in users:
    number_of_messages = users[user]["sent"] + users[user]["received"]
    print(f"{user} - {number_of_messages}")
