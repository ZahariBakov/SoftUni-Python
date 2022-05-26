budget = int(input())

command = input()
bankrupt = False

while command != "End":
    price = int(command)
    if budget < price:
        print("You went in overdraft!")
        bankrupt = True
        break
    else:
        budget -= price
    command = input()

else:
    print("You bought everything needed.")
