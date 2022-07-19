from collections import defaultdict

string = input().replace(" ", "")
characters_dictionary = defaultdict(int)

for char in string:
    characters_dictionary[char] += 1

data = [f"{key} -> {value}" for key, value in characters_dictionary.items()]
print("\n".join(data))
