import math

serial_name = input()
episode_time = int(input())
lunch_break_time = int(input())

lunch_time = lunch_break_time / 8
rest_time = lunch_break_time / 4
free_time = lunch_break_time - lunch_time - rest_time
difference = abs(free_time - episode_time)

if free_time < episode_time:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(difference)} more minutes.")
else:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(difference)} minutes free time.")
