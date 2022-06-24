import math

number_of_students = int(input())
number_of_lecture = int(input())
additional_bonus = int(input())

max_bonus_point = 0
current_students_attendance = 0

for student in range(number_of_students):
    attendance = int(input())
    current_students_bonus = attendance / number_of_lecture * (5 + additional_bonus)
    if current_students_bonus > max_bonus_point:
        max_bonus_point = current_students_bonus
        current_students_attendance = attendance

print(f"Max Bonus: {math.ceil(max_bonus_point)}.")
print(f"The student has attended {current_students_attendance} lectures.")
