first_player_eggs = int(input())
second_player_eggs = int(input())

winner = input()
out_of_eggs = False

while winner != "End of battle":
    if winner == "one":
        second_player_eggs -= 1
    else:
        first_player_eggs -= 1
    if first_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
        out_of_eggs = True
        break
    if second_player_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
        out_of_eggs = True
        break
    winner = input()

if not out_of_eggs:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")
