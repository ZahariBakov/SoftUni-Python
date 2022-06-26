books_shelf = input().split("&")

while True:
    command = input()

    if command == "Done":
        break

    elif "Add " in command:
        book = command.split("| ")[1]

        if book not in books_shelf:
            books_shelf.insert(0, book)

    elif "Take" in command:
        book = command.split(" | ")[1]

        if book in books_shelf:
            books_shelf.remove(book)

    elif "Swap" in command:
        first_book = command.split(" | ")[1]
        second_book = command.split(" | ")[2]

        if first_book in books_shelf and second_book in books_shelf:
            first_index = books_shelf.index(first_book)
            second_index = books_shelf.index(second_book)
            books_shelf[first_index], books_shelf[second_index] = books_shelf[second_index], books_shelf[first_index]

    elif "Insert" in command:
        book = command.split(" | ")[1]

        if book not in books_shelf:
            books_shelf.append(book)

    elif "Check" in command:
        index = int(command.split(" | ")[1])

        if 0 <= index < len(books_shelf):
            print(books_shelf[index])

print(", ".join(books_shelf))
