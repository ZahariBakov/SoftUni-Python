number_of_people = int(input())
lift_condition = list(map(int, input().split()))
lift_condition_string = []

for people in range(len(lift_condition)):
    adding_people = 4 - lift_condition[people]
    if adding_people <= number_of_people:
        number_of_people -= adding_people
        lift_condition[people] += adding_people
    else:
        lift_condition[people] += number_of_people
        number_of_people -= number_of_people

if number_of_people == 0 and lift_condition[-1] != 4:
    print("The lift has empty spots!")
elif lift_condition[-1] == 4 and number_of_people > 0:
    print(f"There isn't enough space! {number_of_people} people in a queue!")

lift_condition_string = list(map(str, lift_condition))
print(" ".join(lift_condition_string))
