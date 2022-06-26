all_vehicle = input().split(">>")

total_tax = 0

for car in all_vehicle:

    year_in_use = int(car.split()[1])
    kilometers_of_car = int(car.split()[2])

    if "family" in car:
        current_vehicle_tax = ((kilometers_of_car // 3000) * 12) + (50 - (year_in_use * 5))
        total_tax += current_vehicle_tax
        print(f"A family car will pay {current_vehicle_tax:.2f} euros in taxes.")

    elif "heavyDuty" in car:
        current_vehicle_tax = ((kilometers_of_car // 9000) * 14) + (80 - (year_in_use * 8))
        total_tax += current_vehicle_tax
        print(f"A heavyDuty car will pay {current_vehicle_tax:.2f} euros in taxes.")

    elif "sports" in car:
        current_vehicle_tax = ((kilometers_of_car // 2000) * 18) + (100 - (year_in_use * 9))
        total_tax += current_vehicle_tax
        print(f"A sports car will pay {current_vehicle_tax:.2f} euros in taxes.")

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
