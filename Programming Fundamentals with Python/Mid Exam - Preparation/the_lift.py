people = int(input())
lift = list(map(int, input().split()))
index = 0
adding_people = 0

for i in range(len(lift)):
    adding_people = 4 - lift[i]
    if adding_people < people:
        people -= adding_people
        lift[i] += adding_people
    else:
        lift[i] += people
        people -= people


if people > 0 and lift[-1] == 4:
    print(f"There isn't enough space! {people} people in a queue!")
elif people == 0 and lift[-1] < 4:
    print("The lift has empty spots!")

lift_as_string = list(map(str, lift))
print(" ".join(lift_as_string))
