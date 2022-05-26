square_meters = float(input())
price = square_meters * 7.61
discount = price * 0.18
final_price = price - discount

print(f"The final price is: %.2f lv." %final_price)
print(f"The discount is: %.2f lv." %discount)
