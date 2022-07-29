def adding_cars(cars):
    numbers_of_cars = int(input())

    for _ in range(numbers_of_cars):
        current_car = input().split("|")
        car = current_car[0]
        mileage = int(current_car[1])
        fuel = int(current_car[2])
        cars[car] = {"mileage": mileage, "fuel": fuel}

    return cars


def vehicle_operations(cars):
    command = input()

    while command != "Stop":
        command = command.split(" : ")
        current_operation = command[0]
        car = command[1]

        if current_operation == "Drive":
            distance = int(command[2])
            fuel = int(command[3])

            if cars[car]["fuel"] < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars[car]["mileage"] += distance
                cars[car]["fuel"] -= fuel
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars[car]["mileage"] >= 100000:
                print(f"Time to sell the {car}!")
                cars.pop(car)

        elif current_operation == "Refuel":
            fuel = int(command[2])

            if cars[car]["fuel"] + fuel > 75:
                fuel = 75 - cars[car]["fuel"]

            cars[car]["fuel"] += fuel

            print(f"{car} refueled with {fuel} liters")

        elif current_operation == "Revert":
            kilometers = int(command[2])
            cars[car]["mileage"] -= kilometers

            if cars[car]["mileage"] < 10000:
                cars[car]["mileage"] = 10000

            else:
                print(f"{car} mileage decreased by {kilometers} kilometers")

        command = input()

    for car in cars:
        print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")

    return cars


collection_of_cars = {}

adding_cars(collection_of_cars)
vehicle_operations(collection_of_cars)
