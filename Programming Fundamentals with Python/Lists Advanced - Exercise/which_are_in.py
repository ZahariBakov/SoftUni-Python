first_list = input().split(", ")
second_list = input().split(", ")

new_list = []

for word in first_list:
    for second_word in second_list:
        if word in second_word:
            new_list.append(word)
            break

print(new_list)
