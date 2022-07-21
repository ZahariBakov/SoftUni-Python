number_of_students = int(input())

students_dict = {}

for i in range(number_of_students):
    current_student = input()
    current_grade = float(input())

    if current_student not in students_dict:
        students_dict[current_student] = []

    students_dict[current_student].append(current_grade)

for key in students_dict:
    average_grade = sum(students_dict[key]) / len(students_dict[key])
    students_dict[key] = f"{average_grade:.2f}"
    if average_grade >= 4.5:
        print(f"{key} -> {students_dict[key]}")
