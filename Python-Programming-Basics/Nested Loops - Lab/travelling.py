destination = input()

while destination != "End":
    trip_cost = float(input())
    saved_money = 0
    while saved_money < trip_cost:
        current_money = float(input())
        saved_money += current_money

    print(f"Going to {destination}!")
    destination = input()
