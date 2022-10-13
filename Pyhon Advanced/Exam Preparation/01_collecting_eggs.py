from collections import deque

eggs_sequence = deque(int(x) for x in input().split(", "))
paper_sequence = [int(x) for x in input().split(", ")]
boxes = 0

while eggs_sequence and paper_sequence:
    current_egg = eggs_sequence.popleft()

    if current_egg == 13:
        paper_sequence[0], paper_sequence[-1] = paper_sequence[-1], paper_sequence[0]

    elif current_egg <= 0:
        continue

    else:
        current_package = current_egg + paper_sequence.pop()

        if current_package <= 50:
            boxes += 1

if boxes == 0:
    print("Sorry! You couldn't fill any boxes!")
else:
    print(f"Great! You filled {boxes} boxes.")

if eggs_sequence:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_sequence)}")
if paper_sequence:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_sequence)}")
