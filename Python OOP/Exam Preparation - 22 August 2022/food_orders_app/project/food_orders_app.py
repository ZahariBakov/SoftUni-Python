from project.client import Client


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __find_client(self, phone_number: str):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __find_meal(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal

    def __check_meal_is_in_menu(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return True

    def register_client(self, client_phone_number: str):
        if client_phone_number in [c.phone_number for c in self.clients_list]:
            raise Exception("The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        self.__validate_menu()

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__validate_menu()

        if client_phone_number not in [c.phone_number for c in self.clients_list]:
            self.register_client(client_phone_number)

        current_client = self.__find_client(client_phone_number)

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            if not self.__check_meal_is_in_menu(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = self.__find_meal(meal_name)
            if current_meal.quantity < meal_quantity:
                raise Exception(f"Not enough quantity of {type(current_meal).__name__}: {meal_name}!")

        for meal_name, meal_quantity in meal_names_and_quantities.items():
            current_meal = self.__find_meal(meal_name)
            current_client.shopping_cart.append(current_meal)
            current_client.bill += current_meal.price * meal_quantity
            current_meal.quantity -= meal_quantity
            current_client.ordered_meals[current_meal.name] = meal_quantity

        ordered_meals_names = []
        for ordered_meal in current_client.shopping_cart:
            ordered_meals_names.append(ordered_meal.name)

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(ordered_meals_names)} for " \
               f"{current_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        current_client = self.__find_client(client_phone_number)

        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for meal_name, meal_quantity in current_client.ordered_meals.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += meal_quantity

        current_client.shopping_cart = []
        current_client.bill = 0.0
        current_client.ordered_meals = {}

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        current_client = self.__find_client(client_phone_number)

        if len(current_client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        total_paid_money = current_client.bill
        current_client.shopping_cart = []
        current_client.bill = 0.0
        current_client.ordered_meals = {}
        self.receipt_id += 1

        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu " \
               f"and {len(self.clients_list)} clients."
