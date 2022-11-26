from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.integer_list = IntegerList("5", 5, 5.5, 1, False, 7)

    def test_correct_initialized(self):
        self.assertEqual([5, 1, 7], self.integer_list._IntegerList__data)

    def test_correct_get_data(self):
        self.assertEqual([5, 1, 7], self.integer_list.get_data())

    def test_add_with_integer_number(self):
        self.integer_list.add(9)

        expected = [5, 1, 7, 9]
        self.assertEqual(expected,  self.integer_list.get_data())
        self.assertEqual(expected, self.integer_list._IntegerList__data)

    def test_add_with_non_integer_number(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("9")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_with_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_with_valid_index(self):
        self.integer_list.remove_index(2)

        expected = [5, 1]

        self.assertEqual(expected, self.integer_list._IntegerList__data)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_get_with_invalid_index(self):
        with self.assertRaises(IndexError) as ir:
            self.integer_list.get(3)

        self.assertEqual("Index is out of range", str(ir.exception))

    def test_get_with_valid_index(self):

        expected = 7

        self.assertEqual(expected, self.integer_list.get(2))

    def test_insert_with_invalid_index(self):
        with self.assertRaises(IndexError) as ir:
            self.integer_list.insert(3, 3)

        self.assertEqual("Index is out of range", str(ir.exception))

    def test_insert_with_invalid_number(self):
        with self.assertRaises(ValueError) as vr:
            self.integer_list.insert(1, "3")

        self.assertEqual("Element is not Integer", str(vr.exception))

    def test_insert_with_correct_index_and_number(self):
        self.integer_list.insert(1, 3)

        expected = [5, 3, 1, 7]

        self.assertEqual(expected, self.integer_list._IntegerList__data)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_get_biggest_number_correct(self):
        self.assertEqual(7, self.integer_list.get_biggest())

    def test_get_index_number_correct(self):
        self.assertEqual(2, self.integer_list.get_index(7))


if __name__ == '__main__':
    main()
