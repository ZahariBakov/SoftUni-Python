def valid_username(data):
    for user in data:
        new_word = ""
        if 3 <= len(user) <= 16:
            for character in user:
                if ord(character) == 45 or ord(character) == 95 or character.isalnum():
                    new_word += character

            if new_word == user:
                print(user)


users_list = input().split(", ")

valid_username(users_list)
