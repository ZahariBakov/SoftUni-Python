lilys_age = int(input())
laundry_price = float(input())
price_per_toy = int(input())

sum = 0
number_of_toys = 0
birthday_money = 0

for i in range(1, lilys_age + 1):
    if i % 2 != 0:
        number_of_toys += 1
    else:
        birthday_money += 10
        sum += birthday_money - 1

sum += number_of_toys * price_per_toy
difference = abs(laundry_price - sum)

if sum >= laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
