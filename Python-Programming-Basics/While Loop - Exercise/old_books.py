searched_book = input()
current_book = input()

checked_book = 0
found_book = False

while current_book != "No More Books":
    if current_book == searched_book:
        found_book = True
        break
    checked_book += 1
    current_book = input()

if found_book:
    print(f"You checked {checked_book} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_book} books.")
