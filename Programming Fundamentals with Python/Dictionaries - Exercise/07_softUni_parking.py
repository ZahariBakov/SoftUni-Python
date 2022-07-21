number_of_users = int(input())
users_dict = {}

for user in range(number_of_users):
    command = input().split(" ")
    current_operation = command[0]
    current_user = command[1]

    if "register" == current_operation:
        current_license_plate = command[2]
        if current_user in users_dict:
            print(f"ERROR: already registered with plate number {users_dict[current_user]}")
        else:
            users_dict[current_user] = current_license_plate
            print(f"{current_user} registered {current_license_plate} successfully")

    else:
        if current_user not in users_dict:
            print(f"ERROR: user {current_user} not found")

        else:
            del users_dict[current_user]
            print(f"{current_user} unregistered successfully")

for user in users_dict:
    print(f"{user} => {users_dict[user]}")
