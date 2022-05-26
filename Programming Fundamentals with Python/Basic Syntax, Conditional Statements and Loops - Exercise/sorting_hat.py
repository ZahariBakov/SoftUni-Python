student_name = ""

while True:
    student_name = input()
    if student_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif student_name == "Voldemort":
        print("You must not speak of that name!")
        break
    elif 5 > len(student_name):
        print(f"{student_name} goes to Gryffindor.")
    elif 5 == len(student_name):
        print(f"{student_name} goes to Slytherin.")
    elif 6 == len(student_name):
        print(f"{student_name} goes to Ravenclaw.")
    elif 6 < len(student_name):
        print(f"{student_name} goes to Hufflepuff.")
