energy = int(input())

command = input()
win = 0

while command != "End of battle":
    distance = int(command)
    if distance > energy:
        print(f"Not enough energy! Game ends with {win} won battles and {energy} energy")
        break

    energy -= distance
    win += 1

    if win % 3 == 0:
        energy += win

    command = input()

if command == "End of battle":
    print(f"Won battles: {win}. Energy left: {energy}")
