from collections import deque

# First decision:

# petrol_pumps = int(input())
# fuels = deque()
# kilometers = deque()
#
# for _ in range(petrol_pumps):
#     command = input().split()
#     fuels.append(int(command[0]))
#     kilometers.append(int(command[1]))
#
# for attempt in range(petrol_pumps):
#     tank = 0
#     failed = False
#
#     for idx in range(petrol_pumps):
#         tank += fuels[idx] - kilometers[idx]
#
#         if tank < 0:
#             failed = True
#             break
#
#     if failed:
#         fuels.append(fuels.popleft())
#         kilometers.append(kilometers.popleft())
#
#     else:
#         print(attempt)
#         break

# Second decision:

n = int(input())
pumps = deque()

for _ in range(n):
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)

for attempt in range(n):
    tank = 0
    failed = False

    for fuel, distance in pumps:
        tank += fuel

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance

    if failed:
        # pumps.append(pumps.popleft())
        pumps.rotate(-1)
    else:
        print(attempt)
        break
