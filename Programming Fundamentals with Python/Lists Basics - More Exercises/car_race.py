sequence_of_numbers = input().split(" ")

left_race_car_time = 0
right_race_car_time = 0
half_steps = len(sequence_of_numbers) // 2

for step in range(half_steps):
    current_time = int(sequence_of_numbers[step])
    if current_time == 0:
        left_race_car_time *= 0.8
    else:
        left_race_car_time += current_time

for step in range(-1, -(half_steps + 1), -1):
    current_time = int(sequence_of_numbers[step])
    if current_time == 0:
        right_race_car_time *= 0.8
    else:
        right_race_car_time += current_time

if left_race_car_time < right_race_car_time:
    print(f"The winner is left with total time: {left_race_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_race_car_time:.1f}")


