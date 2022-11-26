from unittest import TestCase, main
from cat import Cat


class CatTest(TestCase):
    def setUp(self):
        self.cat = Cat("Test")

    def test_cat_size_increased_after_eating(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_raise_error_after_cat_is_already_fed(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_raise_error_if_cat_is_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_cannot_sleep_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
