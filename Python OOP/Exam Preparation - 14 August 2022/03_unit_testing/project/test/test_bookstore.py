from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(15)
        self.books = {
            "Java for dummies": 8,
            "C++ Bible": 3
        }

    def test_correct_initialized(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_books_limit_with_zero_book_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_correct__len__method(self):
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(11, len(self.store))

    def test_not_enough_space_to_receive_book_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Python Advanced", 5)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_add_new_book_correct(self):
        result = self.store.receive_book("Python Advanced", 3)
        expected = "3 copies of Python Advanced are available in the bookstore."

        self.assertEqual(expected, result)

        self.assertEqual({"Python Advanced": 3}, self.store.availability_in_store_by_book_titles)

    def test_add_existing_book_correct(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.receive_book("Java for dummies", 2)
        expected = "10 copies of Java for dummies are available in the bookstore."

        self.assertEqual(expected, result)

    def test_sell_non_existing_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Python Advanced", 3)

        self.assertEqual("Book Python Advanced doesn't exist!", str(ex.exception))

    def test_sell_more_copies_than_available_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("C++ Bible", 5)

        expected = "C++ Bible has not enough copies to sell. Left: 3"
        self.assertEqual(expected, str(ex.exception))

    def test_correct_sell_books(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.sell_book("Java for dummies", 3)
        expected = "Sold 3 copies of Java for dummies"

        self.assertEqual(expected, result)

        self.assertEqual(3, self.store.total_sold_books)

        self.assertEqual({
            "Java for dummies": 5,
            "C++ Bible": 3
        }, self.store.availability_in_store_by_book_titles)

    def test_correct__str__methods(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(
            "Total sold books: 0\n"
            'Current availability: 11\n'
            ' - Java for dummies: 8 copies\n'
            ' - C++ Bible: 3 copies',
            str(self.store)
        )


if __name__ == '__main__':
    main()
