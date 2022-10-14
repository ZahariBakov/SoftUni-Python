def shopping_list(money, **kwargs):
    basket = ''
    len_basket = 0

    if money < 100:
        basket = "You do not have enough budget."

    else:
        for product, value in kwargs.items():
            sum = float(value[0]) * int(value[1])

            if sum < money:
                basket += f"You bought {product} for {sum:.2f} leva.\n"
                money -= sum
                len_basket += 1

                if len_basket == 5:
                    break

    return basket


print(shopping_list(
    100,
    microwave=(70, 2),
    skirts=(15, 4),
    coffee=(1.50, 10),
))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
