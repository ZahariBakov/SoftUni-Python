from collections import deque

players_string = input()
tosses_count = int(input())

player = deque(players_string.split(" "))
current_toss = 0

while len(player) > 1:
    current_toss += 1
    current_player = player.popleft()

    if current_toss == tosses_count:
        current_toss = 0
        print(f"Removed {current_player}")

    else:
        player.append(current_player)

winner = player.popleft()
print(f"Last is {winner}")
