first_list = input().split(", ")
second_list = input().split(", ")

new_list = []

for first_word in first_list:
    for second_word in second_list:
        if first_word in second_word:
            new_list.append(first_word)
            break

print(new_list)
