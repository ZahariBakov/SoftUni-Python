available_products = input().split(" ")
searched_products = input().split(" ")

products_dict = {available_products[i]: int(available_products[i + 1]) for i in range(0, len(available_products), 2)}

for product in searched_products:

    if product in products_dict:
        print(f"We have {products_dict[product]} of {product} left")

    else:
        print(f"Sorry, we don't have {product}")
