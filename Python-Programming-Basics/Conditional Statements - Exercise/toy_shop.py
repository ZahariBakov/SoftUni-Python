trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzles_price = number_of_puzzles * 2.60
dolls_price = number_of_dolls * 3
bears_price = number_of_bears * 4.10
minions_price = number_of_minions * 8.20
trucks_price = number_of_trucks * 2

total_number = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
toys_price = puzzles_price + dolls_price + bears_price + minions_price + trucks_price

if total_number >= 50:
    toys_price -= toys_price * 0.25
profit = toys_price - toys_price * 0.1
difference = abs(trip_price - profit)

if profit < trip_price:
    print(f"Not enough money! {difference:.2f} lv needed.")
else:
    print(f"Yes! {difference:.2f} lv left.")
