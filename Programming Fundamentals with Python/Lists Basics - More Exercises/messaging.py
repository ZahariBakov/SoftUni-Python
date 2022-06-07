sequence_of_numbers = input().split(" ")
string = input()
message = ""
string_list = []

for char in string:
    string_list.append(char)

for i in sequence_of_numbers:
    index = 0
    for j in i:
        index += int(j)
    if index > len(string_list):
        index = index - len(string_list)
    print(string_list[index], end="")
    string_list.pop(index)




