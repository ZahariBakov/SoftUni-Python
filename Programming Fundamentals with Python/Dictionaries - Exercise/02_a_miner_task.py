from collections import defaultdict

resources_dictionary = defaultdict(int)

while True:
    command = input()
    if command == "stop":
        break

    value = int(input())
    resources_dictionary[command] += value

data = [f"{key} -> {value}" for key, value in resources_dictionary.items()]
print("\n".join(data))
