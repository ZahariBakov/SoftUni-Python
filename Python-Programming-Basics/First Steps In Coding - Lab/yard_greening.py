square_meters = float(input())
total_price = 7.61 * square_meters
discount = 0.18 * total_price
total_price_with_discount = total_price - discount

print(f"The final price is: {total_price_with_discount} lv.")
print(f"The discount is: {discount} lv.")
