def valid_length(data):
    if 3 <= len(data) <= 16:
        return True
    return False


def characters_are_valid(data):
    for character in data:
        if not (character == "-" or character == "_" or character.isalnum()):
            return False
    return True


def no_redundant_symbols(data):
    if " " in data:
        return False
    return True


def valid_user(data):
    if valid_length(data) and characters_are_valid(data) and no_redundant_symbols(data):
        return True
    return False


users_list = input().split(", ")
for user in users_list:
    if valid_user(user):
        print(user)
