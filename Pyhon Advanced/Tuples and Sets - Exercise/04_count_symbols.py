text = input()
characters_dict = {}

for ch in text:
    if ch not in characters_dict:
        characters_dict[ch] = 0

    characters_dict[ch] += 1

sorted_list = sorted(characters_dict)

for el in sorted_list:
    print(f"{el}: {characters_dict[el]} time/s")
