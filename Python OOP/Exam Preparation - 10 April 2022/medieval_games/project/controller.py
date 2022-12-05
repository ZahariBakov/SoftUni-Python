class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_las_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, - 1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)

        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        elif supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def __find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player

    @staticmethod
    def __check_cannot_duel(*args):
        result = []
        for player in args:
            if player.stamina == 0:
                result.append(f"Player {player.name} does not have enough stamina.")

        if result:
            return "\n".join(result)

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)

        if p1.stamina < p2.stamina:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    def add_player(self, *args):
        result = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                result.append(player.name)

        return f'Successfully added: {", ".join(result)}'

    def add_supply(self, *args):
        for product in args:
            self.supplies.append(product)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        supply = self.__find_las_supply(sustenance_type)

        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        result = self.__check_cannot_duel(first_player, second_player)
        if result:
            return result

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= (player.age * 2)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(str(supply.details()))

        return '\n'.join(result)
