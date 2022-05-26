students_name = input()

excluded_sum = 0
excluded = False
total_evaluation = 0
current_class = 1

while current_class <= 12:
    current_evaluation = float(input())
    if current_evaluation < 4:
        excluded_sum += 1
        if excluded_sum > 1:
            excluded = True
            break
    else:
        total_evaluation += current_evaluation
        current_class += 1
        excluded_sum = 0


if excluded:
    print(f"{students_name} has been excluded at {current_class} grade")
else:
    average_evaluation = total_evaluation / 12
    print(f"{students_name} graduated. Average grade: {average_evaluation:.2f}")
