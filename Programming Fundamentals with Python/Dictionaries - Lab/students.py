students_dict = {}

while True:
    command = input().split(":")

    if len(command) > 1:
        name, id, course = command
        if course not in students_dict:
            students_dict[course] = {}
        students_dict[course][name] = id

    else:
        break

course_name = command[0].replace("_", " ")

for name, id in students_dict[course_name].items():
    print(f'{name} - {id}')
