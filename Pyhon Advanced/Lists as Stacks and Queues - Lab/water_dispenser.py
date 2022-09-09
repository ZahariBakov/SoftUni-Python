from collections import deque

quantity = int(input())
queue = deque()

while True:
    command = input()

    if command == "Start":
        break

    else:
        queue.append(command)

while True:
    command = input()

    if command == "End":
        print(f"{quantity} liters left")
        break

    elif "refill" in command:
        current_water = int(command.split(" ")[1])
        quantity += current_water

    else:
        current_water = int(command)
        current_person = queue.popleft()

        if quantity >= current_water:
            quantity -= current_water
            print(f"{current_person} got water")

        else:
            print(f"{current_person} must wait")
