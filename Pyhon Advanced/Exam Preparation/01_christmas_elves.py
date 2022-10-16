from collections import deque

elves = deque([int(x) for x in input().split()])
boxes = [int(y) for y in input().split()]
toys = 0
energy = 0
count = 0

while elves and boxes:
    if elves[0] < 5:
        elves.popleft()
        continue
    count += 1
    if count % 3 == 0 and count % 5 == 0:
        if elves[0] >= boxes[-1] * 2:
            elves[0] -= boxes[-1] * 2
            energy += boxes.pop() * 2
            elves.append(elves.popleft())
        else:
            elves[0] *= 2
            elves.append(elves.popleft())
    elif count % 3 == 0:
        if elves[0] >= boxes[-1] * 2:
            toys += 2
            energy += boxes[-1] * 2
            elves[0] -= boxes.pop() * 2
            elves[0] += 1
            elves.append(elves.popleft())
        else:
            elves[0] *= 2
            elves.append(elves.popleft())
    elif count % 5 == 0:
        if elves[0] >= boxes[-1]:
            elves[0] -= boxes[-1]
            energy += boxes.pop()
            elves.append(elves.popleft())
        else:
            elves[0] *= 2
            elves.append(elves.popleft())
    elif elves[0] >= boxes[-1]:
        toys += 1
        energy += boxes[-1]
        elves[0] -= boxes.pop() - 1
        elves.append(elves.popleft())
    else:
        elves[0] *= 2
        elves.append(elves.popleft())

print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elves:
    print(f"Elves left: {', '.join(str(x) for x in elves)}")
if boxes:
    print(f"Boxes left: {', '.join(str(y) for y in boxes)}")
