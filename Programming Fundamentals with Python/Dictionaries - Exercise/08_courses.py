courses = {}

while True:
    command = input()

    if command == "end":
        break

    course_name = command.split(" : ")[0]
    students_name = command.split(" : ")[1]

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(students_name)

for key in courses:
    print(f"{key}: {len(courses[key])}")
    [print(f"-- {student_name}") for student_name in courses[key]]
