team_a = list(range(1, 12))
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input().split(" ")
game_was_terminated = False
team_a_cards = []
team_b_cards = []

for card in cards:
    current_card = card.split("-")
    team = current_card[0]
    player = int(current_card[1])
    if team == "A":
        if player in team_a_cards:
            continue
        team_a.remove(player)
        team_a_cards.append(player)
        if len(team_a) < 7:
            game_was_terminated = True
            break
    else:
        if player in team_b_cards:
            continue
        team_b.remove(player)
        team_b_cards.append(player)
        if len(team_b) < 7:
            game_was_terminated = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:
    print("Game was terminated")




