def shopping_cart(*args):
    result = ''
    meals = {
        "Pizza": [],
        "Dessert": [],
        "Soup": []
    }

    for el in args:
        if "Stop" in el:
            break
        meal, product = el
        for meal_type, number_product in (("Pizza", 4), ("Soup", 3), ("Dessert", 2)):
            if meal == meal_type and len(meals[meal]) != number_product and product not in meals[meal]:
                meals[meal].append(product)

    for p_meal, p_product in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{p_meal}:\n"
        for item in sorted(p_product):
            result += f" - {item}\n"

    if len(result) == 22:
        result = "No products in the cart!"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
