from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_driver(self, driver_name):
        driver = [d for d in self.drivers if d.name == driver_name]
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        return driver[0]

    def __find_car(self, car_type):
        car = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        return car[-1]

    def __find_race(self, race_name):
        race = [r for r in self.races if r.name == race_name]
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        return race[0]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        if car_type == "MuscleCar":
            self.cars.append(MuscleCar(model, speed_limit))
            return f"{car_type} {model} is created."
        elif car_type == "SportsCar":
            self.cars.append(SportsCar(model, speed_limit))
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        car = self.__find_car(car_type)
        car.is_taken = True

        if driver.car:
            old_car = driver.car
            old_car.is_taken = False
            driver.car = car
            return f'Driver {driver_name} changed his car from {old_car.model} to ' \
                   f'{car.model}.'

        driver.car = car
        return f'Driver {driver_name} chose the car {car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        driver = self.__find_driver(driver_name)

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver_name in [d.name for d in race.drivers]:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 "
                            f"participants!")

        winner = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]
        result = []

        for driver in winner:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a"
                          f" speed of {driver.car.speed_limit}.")

        return "\n".join(result)
