annual_tax = int(input())

sneakers_price = annual_tax * 0.6
outfit_price = sneakers_price * 0.8
ball_price = outfit_price / 4
accessories_price = ball_price / 5

total_price = annual_tax + sneakers_price + outfit_price + ball_price + accessories_price

print(total_price)
