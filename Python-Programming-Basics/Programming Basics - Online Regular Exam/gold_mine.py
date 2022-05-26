mine_number = int(input())

for current_mine in range(mine_number):
    expected_gold = float(input())
    day_of_work = int(input())
    mined_gold = 0
    for current_day in range(day_of_work):
        gold_per_day = float(input())
        mined_gold += gold_per_day
    average_mined_gold = mined_gold / day_of_work
    if average_mined_gold >= expected_gold:
        print(f"Good job! Average gold per day: {average_mined_gold:.2f}.")
    else:
        difference = expected_gold - average_mined_gold
        print(f"You need {difference:.2f} gold.")
