def shopping_cart(*args):
    meals = {
        "Pizza": [],
        "Dessert": [],
        "Soup": []
    }

    for el in args:
        meal = el[0]
        product = el[1]
        if el == "Stop":
            break
        if meal == "Pizza" and len(meals[meal]) == 4:
            continue
        elif meal == "Soup" and len(meals[meal]) == 3:
            continue
        elif meal == "Desert" and len(meals[meal]) == 2:
            continue
        if product not in meals[meal]:
            meals[meal].append(product)

    for value in meals.values():
        if len(value) > 0:
            break
    else:
        return "No products in the cart!"

    sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ''
    for el in sorted_meals:
        result += f"{el[0]}:\n"
        sorted_products = sorted(el[1])
        for product in sorted_products:
            result += f" - {product}\n"

    return result


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
