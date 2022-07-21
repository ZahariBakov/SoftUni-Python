languages_dict = {}
users_dict = {}

while True:
    command = input()

    if command == "exam finished":
        break

    if "banned" in command:
        user = command.split("-")[0]
        del users_dict[user]
        continue

    user, language, point = command.split("-")

    if user not in users_dict:
        users_dict[user] = int(point)

    if language not in languages_dict:
        languages_dict[language] = 0

    languages_dict[language] += 1

    if user in users_dict and language in languages_dict:
        if users_dict[user] < int(point):
            users_dict[user] = int(point)

print("Results:")
for key, value in users_dict.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in languages_dict.items():
    print(f"{key} - {value}")
