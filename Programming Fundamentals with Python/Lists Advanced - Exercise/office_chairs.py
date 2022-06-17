rooms = int(input())
free_chair = 0
all_room_have_chair = True

for room in range(1, rooms + 1):
    current_room = input().split()
    chair = current_room[0].count("X")
    visitors = int(current_room[1])
    if chair < visitors:
        print(f"{visitors - chair} more chairs needed in room {room}")
        all_room_have_chair = False
    else:
        free_chair += chair - visitors

if all_room_have_chair:
    print(f"Game On, {free_chair} free chairs left")
