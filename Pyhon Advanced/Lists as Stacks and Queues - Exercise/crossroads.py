from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
passed_cars = 0
crash = False

command = input()

while command != "END":
    if command == "green":
        time = green_light
        if cars:
            while cars and time > 0:
                current_car = cars.popleft()

                if time + free_window < len(current_car):
                    crash_char = current_car[time + free_window]
                    print("A crash happened!")
                    print(f"{current_car} was hit at {crash_char}.")
                    crash = True
                    break
                else:
                    passed_cars += 1
                    time -= len(current_car)

    else:
        cars.append(command)

    if crash:
        break

    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
