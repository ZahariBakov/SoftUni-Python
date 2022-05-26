numbers_of_groups = int(input())

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
total_people = 0

for i in range(numbers_of_groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group < 6:
        group1 += people_in_group
    elif people_in_group < 13:
        group2 += people_in_group
    elif people_in_group < 26:
        group3 += people_in_group
    elif people_in_group < 41:
        group4 += people_in_group
    else:
        group5 += people_in_group

print(f"{group1 / total_people * 100:.2f}%")
print(f"{group2 / total_people * 100:.2f}%")
print(f"{group3 / total_people * 100:.2f}%")
print(f"{group4 / total_people * 100:.2f}%")
print(f"{group5 / total_people * 100:.2f}%")
