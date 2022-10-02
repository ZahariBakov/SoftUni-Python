numbers_dictionary = {}

search = False
remove = False

while True:
    line = input()

    if line == "Search":
        search = True
        continue

    elif line == "Remove":
        remove = True
        continue

    elif line == "End":
        break

    if not search:

        number_as_string = line

        try:
            number = int(input())
            numbers_dictionary[number_as_string] = number
        except ValueError:
            print("The variable number must be an integer")

    elif not remove:
        searched = line

        try:
            print(numbers_dictionary[searched])
        except NameError:
            print("Number does not exist in dictionary")

    else:
        searched = line

        try:
            del numbers_dictionary[searched]
        except KeyError:
            print("Number does not exist in dictionary")

print(numbers_dictionary)
