def naughty_or_nice_list(kids, *args, **kwargs):
    kids_dict = {"Nice": [], "Naughty": [], "Not found": []}
    for command in args:
        number, position = command.split('-')
        current_number = 0
        for el in kids:
            if el[0] == int(number):
                current_number += 1
        if current_number == 1:
            for idx, el in enumerate(kids):
                if el[0] == int(number):
                    kids_dict[position].append(el[1])
                    kids.pop(idx)

    for name, position in kwargs.items():
        current_name = 0
        for el in kids:
            if el[1] == name:
                current_name += 1
        if current_name == 1:
            for idx, el in enumerate(kids):
                if el[1] == name:
                    kids_dict[position].append(name)
                    kids.pop(idx)
    for el in kids:
        kids_dict["Not found"].append(el[1])

    output = ''
    for key, value in kids_dict.items():
        if value:
            output += f"{key}: {', '.join(value)}\n"

    return output


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
