from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shop = ShoppingCart("Test", 200.5)

    def test_correct_initialized(self):
        self.assertEqual("Test", self.shop.shop_name)
        self.assertEqual(200.5, self.shop.budget)
        self.assertEqual({}, self.shop.products)

    def test_sho_name_not_starts_with_capital_letter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.shop_name = "test"

        expected = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_product_to_cart_with_price_more_than_limited_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart("mushrooms", 150.7)

        expected = "Product mushrooms cost too much!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_product_to_cart_with_correct_price(self):
        result = self.shop.add_to_cart("mushrooms", 99.7)

        self.assertEqual(99.7, self.shop.products["mushrooms"])
        self.assertEqual({'mushrooms': 99.7}, self.shop.products)

        expected = "mushrooms product was successfully added to the cart!"
        self.assertEqual(expected, result)

    def test_remove_invalid_product_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart("cheese")

        expected = "No product with name cheese in the cart!"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_product_with_correct_data(self):
        self.shop.products = {'mushrooms': 99.7, "cheese": 17.8}

        result = self.shop.remove_from_cart("mushrooms")

        self.assertEqual(17.8, self.shop.products["cheese"])
        self.assertEqual({'cheese': 17.8}, self.shop.products)

        expected = "Product mushrooms was successfully removed from the cart!"
        self.assertEqual(expected, result)

    def test__add__method(self):
        second_shop = ShoppingCart("Second", 150.5)
        self.shop.products = {'mushrooms': 99.7}
        second_shop.products = {'cheese': 17.8}

        mix_shop = self.shop.__add__(second_shop)

        self.assertEqual("TestSecond", mix_shop.shop_name)
        self.assertEqual(351.0, mix_shop.budget)
        self.assertEqual({'mushrooms': 99.7, 'cheese': 17.8}, mix_shop.products)

    def test_buy_product_with_no_budget_raise_value_error(self):
        self.shop.budget = 50
        self.shop.add_to_cart("mushrooms", 99)
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()

        expected = "Not enough money to buy the products! Over budget with 49.00lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_product_with_enough_budget(self):
        self.shop.add_to_cart("mushrooms", 99)
        result = self.shop.buy_products()

        expected = 'Products were successfully bought! Total cost: 99.00lv.'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
