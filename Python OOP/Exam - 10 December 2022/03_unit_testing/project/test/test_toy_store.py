from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_correct_initialized(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.toy_store.toy_shelf)

    def test_add_toy_with_non_existing_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("M", "Doll")

        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_correct_shelf_and_toy(self):
        result = self.toy_store.add_toy("A", "Doll")
        expected = "Toy:Doll placed successfully!"
        self.assertEqual(expected, result)
        self.assertEqual("Doll", self.toy_store.toy_shelf["A"])

    def test_add_toy_with_already_added_toy_raise_exception(self):
        self.toy_store.add_toy("A", "Doll")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Doll")

        expected = "Toy is already in shelf!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_toy_to_shelf_not_none_raise_exception(self):
        self.toy_store.add_toy("A", "Doll")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Barbie")

        expected = "Shelf is already taken!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_with_non_existing_shelf_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("M", "Doll")

        expected = "Shelf doesn't exist!"
        self.assertEqual(expected, str(ex.exception))

    def test_remove_toy_with_non_existing_toy_raise_exception(self):
        self.toy_store.add_toy("A", "Barbie")

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Doll")

        expected = "Toy in that shelf doesn't exists!"
        self.assertEqual(expected, str(ex.exception))
        self.assertEqual("Barbie", self.toy_store.toy_shelf["A"])

    def test_remove_toy_with_existing_toy(self):
        self.toy_store.add_toy("A", "Barbie")
        self.toy_store.add_toy("C", "Doll")

        result = self.toy_store.remove_toy("A", "Barbie")
        expected = "Remove toy:Barbie successfully!"
        self.assertEqual(expected, result)
        second_expected = {
            "A": None,
            "B": None,
            "C": "Doll",
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(second_expected, self.toy_store.toy_shelf)


if __name__ == '__main__':
    main()
