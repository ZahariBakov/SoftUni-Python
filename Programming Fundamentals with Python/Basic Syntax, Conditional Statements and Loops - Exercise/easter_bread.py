budget = float(input())
price_per_one_kilo_flour = float(input())

price_for_one_pack_eggs = 0.75 * price_per_one_kilo_flour
price_for_one_liter_milk = 1.25 * price_per_one_kilo_flour
loaf_making = 0
colored_eggs = 0
loaf_price = price_for_one_pack_eggs + price_per_one_kilo_flour + price_for_one_liter_milk / 4

while budget >= loaf_price:
    budget -= loaf_price
    loaf_making += 1
    colored_eggs += 3
    if loaf_making % 3 == 0:
        colored_eggs -= loaf_making - 2

print(f"You made {loaf_making} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
