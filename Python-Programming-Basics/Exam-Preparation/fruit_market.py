strawberries_price_per_kilos = float(input())
bananas_kilograms = float(input())
oranges_kilograms = float(input())
raspberries_kilograms = float(input())
strawberries_kilograms = float(input())

raspberries_price_per_kilo = strawberries_price_per_kilos / 2
oranges_price_per_kilo = 0.6 * raspberries_price_per_kilo
bananas_price_per_kilo = 0.2 * raspberries_price_per_kilo

raspberries_price = raspberries_price_per_kilo * raspberries_kilograms
oranges_price = oranges_price_per_kilo * oranges_kilograms
bananas_price = bananas_price_per_kilo * bananas_kilograms
strawberries_price = strawberries_price_per_kilos * strawberries_kilograms

needed_money = raspberries_price + oranges_price + bananas_price + strawberries_price

print(f"{needed_money:.2f}")
