first_string = input()
second_string = input()

last_string = first_string

for char in range(len(first_string)):
    new_string = second_string[:char + 1]
    old_string = first_string[char + 1:]
    current_string = new_string + old_string
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string
