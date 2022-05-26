chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
veggie_price = veggie_menu * 8.15
total_menu_price = chicken_price + fish_price + veggie_price
dessert_price = total_menu_price * 0.2

final_price = total_menu_price + dessert_price + 2.50

print(final_price)
