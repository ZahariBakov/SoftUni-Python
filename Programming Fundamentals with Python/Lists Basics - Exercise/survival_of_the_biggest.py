list_numbers_as_string = input().split(" ")
remove_number = int(input())

list_of_numbers = []

for num in list_numbers_as_string:
    current_number = int(num)
    list_of_numbers.append(current_number)

for i in range(remove_number):
    min_num = min(list_of_numbers)
    list_of_numbers.remove(min_num)

final_string = ""

for number in list_of_numbers:
    if number == list_of_numbers[-1]:
        final_string += f"{number}"
    else:
        final_string += f"{number}, "

print(final_string)







