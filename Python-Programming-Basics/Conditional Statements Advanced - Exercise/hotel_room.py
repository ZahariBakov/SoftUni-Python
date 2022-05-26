month = input()
nights_num = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = nights_num * 50
    apartment_price = nights_num * 65
    if nights_num > 14:
        studio_price = studio_price * 0.7
        apartment_price = apartment_price * 0.9
    elif nights_num > 7:
        studio_price = studio_price * 0.95
elif month == "June" or month == "September":
    studio_price = nights_num * 75.20
    apartment_price = nights_num * 68.70
    if nights_num > 14:
        studio_price = studio_price * 0.8
        apartment_price = apartment_price * 0.9
elif month == "July" or month == "August":
    studio_price = nights_num * 76
    apartment_price = nights_num * 77
    if nights_num > 14:
        apartment_price = apartment_price * 0.9
print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
