need_money = float(input())
money_on_hand = float(input())

spending_days = 0
spending_too_many_days = False
past_days = 0

while money_on_hand < need_money:
    command = input()
    current_money = float(input())
    past_days += 1
    if command == "save":
        money_on_hand += current_money
        spending_days = 0
    else:
        money_on_hand -= current_money
        spending_days += 1
        if spending_days > 4:
            spending_too_many_days = True
            break
        if money_on_hand < 0:
            money_on_hand = 0

if spending_too_many_days:
    print("You can't save the money.")
    print(f"{past_days}")
else:
    print(f"You saved the money for {past_days} days.")
