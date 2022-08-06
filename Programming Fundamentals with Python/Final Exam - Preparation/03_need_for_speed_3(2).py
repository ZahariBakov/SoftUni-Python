def adding_car(dict, car, mileage, fuel):
    if car not in dict:
        dict[car] = {"mileage": mileage, "fuel": fuel}

    return dict


def drive(dict, car, distance, need_fuel):
    if need_fuel > dict[car]["fuel"]:
        print("Not enough fuel to make that ride")

    else:
        dict[car]["mileage"] += distance
        dict[car]["fuel"] -= need_fuel
        print(f"{car} driven for {distance} kilometers. {need_fuel} liters of fuel consumed.")

    if dict[car]["mileage"] >= 100000:
        del dict[car]
        print(f"Time to sell the {car}!")

    return dict


def refuel(dict, car, fuel):
    if dict[car]["fuel"] + fuel > 75:
        fuel = 75 - dict[car]["fuel"]

    print(f"{car} refueled with {fuel} liters")
    dict[car]["fuel"] += fuel

    return dict


def revert(dict, car, kilometers):
    dict[car]["mileage"] -= kilometers

    if dict[car]["mileage"] < 10000:
        dict[car]["mileage"] = 10000

    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")

    return dict


numbers_of_cars = int(input())

my_cars = {}

for i in range(numbers_of_cars):
    current_car = input().split('|')
    car = current_car[0]
    mileage = int(current_car[1])
    fuel = int(current_car[2])
    adding_car(my_cars, car, mileage, fuel)

while True:
    command = input()

    if command == "Stop":
        break

    command = command.split(" : ")
    car = command[1]

    if "Drive" in command:
        distance = int(command[2])
        fuel_needed = int(command[3])
        drive(my_cars, car, distance, fuel_needed)

    elif "Refuel" in command:
        fuel = int(command[2])
        refuel(my_cars, car, fuel)

    elif "Revert" in command:
        kilometers = int(command[2])
        revert(my_cars, car, kilometers)

for car in my_cars:
    print(f"{car} -> Mileage: {my_cars[car]['mileage']} kms, Fuel in the tank: {my_cars[car]['fuel']} lt.")
