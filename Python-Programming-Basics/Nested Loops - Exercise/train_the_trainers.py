juri = int(input())
presentation = input()

final_score = 0
presentation_num = 0

while presentation != "Finish":
    average_score = 0
    total_score = 0
    presentation_num += 1
    for i in range(juri):
        current_score = float(input())
        total_score += current_score
    average_score = total_score / juri
    final_score += average_score
    print(f"{presentation} - {average_score:.2f}.")

    presentation = input()

final_assessment = final_score / presentation_num
print(f"Student's final assessment is {final_assessment:.2f}.")
