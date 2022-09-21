from collections import deque

green_light = int(input())
free_window = int(input())
time = green_light
cars_and_command = deque()
passed_cars = 0

crash = False

command = input()

while command != "END":
    cars_and_command.append(command)

    command = input()

while cars_and_command:
    command = cars_and_command.popleft()

    if command == "END":
        break

    if command == "green":
        time = green_light

    elif time == 0:
        continue

    else:
        if time + free_window < len(command):
            crash_char = command[time + free_window]
            print("A crash happened!")
            print(f"{command} was hit at {crash_char}.")
            crash = True
            break

        else:
            passed_cars += 1
            time -= len(command)
            if time < 0 :
                time = 0

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
