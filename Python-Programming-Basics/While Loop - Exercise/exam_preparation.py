unsatisfactory_valuations = int(input())
current_problem = input()

total_evaluation = 0
number_of_problem = 0
poor_grades = 0
need_a_break = False
last_problem = ""

while current_problem != "Enough":
    last_problem = current_problem
    number_of_problem += 1
    current_evaluation = int(input())
    total_evaluation += current_evaluation

    if current_evaluation <= 4:
        poor_grades += 1
        if poor_grades >= unsatisfactory_valuations:
            need_a_break = True
            break

    current_problem = input()

if need_a_break:
    print(f"You need a break, {poor_grades} poor grades.")
else:
    average_evaluation = total_evaluation / number_of_problem
    print(f"Average score: {average_evaluation:.2f}")
    print(f"Number of problems: {number_of_problem}")
    print(f"Last problem: {last_problem}")
