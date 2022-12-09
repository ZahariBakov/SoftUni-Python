from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    successful = 0
    unsuccessful = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    @staticmethod
    def __find_astronaut(name, astronauts):
        for astronaut in astronauts:
            if astronaut.name == name:
                return astronaut
        raise Exception(f"Astronaut {name} doesn't exist!")

    @staticmethod
    def __find_planet(planet_name, planets):
        for planet in planets:
            if planet.name == planet_name:
                return planet
        raise Exception("Invalid planet name!")

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        if astronaut_type not in ("Biologist", "Meteorologist", "Geodesist"):
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            self.astronaut_repository.add(Biologist(name))

        elif astronaut_type == "Geodesist":
            self.astronaut_repository.add(Geodesist(name))

        else:
            self.astronaut_repository.add(Meteorologist(name))

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items += items.split(", ")
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.__find_astronaut(name, self.astronaut_repository.astronauts)
        self.astronaut_repository.astronauts.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        suitable_astronauts = {}
        astronaut_on_mission = 0

        planet = self.__find_planet(planet_name, self.planet_repository.planets)

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                suitable_astronauts[astronaut] = astronaut.oxygen
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        suitable_astronauts = dict(sorted(suitable_astronauts.items(),
                                          key=lambda x: x[1], reverse=True))

        for astronaut in suitable_astronauts:
            if not planet.items or astronaut_on_mission == 5:
                break
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            astronaut_on_mission += 1

        if not planet.items:
            self.successful += 1
            return f"Planet: {planet_name} was explored. {astronaut_on_mission}" \
                   f" astronauts participated in collecting items."
        self.unsuccessful += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.successful} successful missions!",
                  f"{self.unsuccessful} missions were not completed!",
                  f"Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            result.append(f"Name: {astronaut.name}")
            result.append(f"Oxygen: {astronaut.oxygen}")

            if astronaut.backpack:
                result.append(f'Backpack items: {", ".join(astronaut.backpack)}')
            else:
                result.append(f"Backpack items: none")

        return "\n".join(result)
