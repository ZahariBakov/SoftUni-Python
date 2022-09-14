from collections import deque

petrol_pumps = int(input())
fuels = deque()
kilometers = deque()

for _ in range(petrol_pumps):
    command = input().split()
    fuels.append(int(command[0]))
    kilometers.append(int(command[1]))

for attempt in range(petrol_pumps):
    tank = 0
    failed = False

    for idx in range(petrol_pumps):
        tank += fuels[idx] - kilometers[idx]

        if tank < 0:
            failed = True
            break

    if failed:
        fuels.append(fuels.popleft())
        kilometers.append(kilometers.popleft())

    else:
        print(attempt)
        break
