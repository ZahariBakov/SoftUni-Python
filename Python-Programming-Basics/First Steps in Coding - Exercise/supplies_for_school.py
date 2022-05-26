pen_package = int(input())
marker_package = int(input())
cleaning_detergent = int(input())
discount_percent = int(input())

pen_price = pen_package * 5.80
marker_price = marker_package * 7.20
detergent_price = cleaning_detergent * 1.20
total_sum = pen_price + marker_price + detergent_price
discount = discount_percent / 100
final_price = total_sum - total_sum * discount

print(final_price)
