increase_money = input()

total_money = 0
sum = 0


while increase_money != "NoMoreMoney":
    if float(increase_money) < 0:
        print("Invalid operation!")
        break
    total_money += float(increase_money)
    print(f"Increase: {float(increase_money):.2f}")
    increase_money = input()

print(f"Total: {total_money:.2f}")
