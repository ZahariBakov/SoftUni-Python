actor_name = input()
current_points = float(input())
number_of_evaluators = int(input())

for i in range(number_of_evaluators):
    evaluators_name = input()
    evaluators_points = float(input())
    current_points += len(evaluators_name) * evaluators_points / 2
    if current_points > 1250.5:
        break

if current_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {current_points:.1f}!")
else:
    difference = 1250.5 - current_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
