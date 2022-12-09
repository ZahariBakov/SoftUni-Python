from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Knijarnicata")

    def test_correct_initialized(self):
        self.assertEqual("Knijarnicata", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_create_library_with_empty_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            second_library = Library("")

        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_book_method(self):
        self.library.add_book("Agatha Christie", "Murder on the Orient Express")
        self.assertEqual({"Agatha Christie": ["Murder on the Orient Express"]}, self.library.books_by_authors)

        self.library.add_book("Agatha Christie", "Giant's Bread")
        self.assertEqual({"Agatha Christie": ["Murder on the Orient Express", "Giant's Bread"]},
                         self.library.books_by_authors)

    def test_add_reader(self):
        self.library.add_reader("John")
        self.assertEqual({"John": []}, self.library.readers)

    def test_add_reader_that_exists(self):
        self.library.add_reader("John")
        result = self.library.add_reader("John")

        expected = "John is already registered in the Knijarnicata library."
        self.assertEqual(expected, result)

    def test_rent_book_with_non_exist_reader(self):
        result = self.library.rent_book("John", "Agatha Christie", "Murder on the Orient Express")
        expected = "John is not registered in the Knijarnicata Library."
        self.assertEqual(expected, result)

    def test_rent_book_with_non_exist_author(self):
        self.library.add_reader("John")
        result = self.library.rent_book("John", "Agatha Christie", "Murder on the Orient Express")
        expected = "Knijarnicata Library does not have any Agatha Christie's books."
        self.assertEqual(expected, result)

    def test_rent_book_with_non_exist_book(self):
        self.library.add_reader("John")
        self.library.add_book("Agatha Christie", "Murder on the Orient Express")
        result = self.library.rent_book("John", "Agatha Christie", "Giant's Bread")
        expected = """Knijarnicata Library does not have Agatha Christie's "Giant's Bread"."""
        self.assertEqual(expected, result)

    def test_rent_book_correct_value(self):
        self.library.add_reader("John")
        self.library.add_book("Agatha Christie", "Murder on the Orient Express")
        self.library.add_book("Agatha Christie", "Giant's Bread")
        self.library.rent_book("John", "Agatha Christie", "Murder on the Orient Express")

        self.assertEqual({"John": [{'Agatha Christie': 'Murder on the Orient Express'}]}, self.library.readers)
        self.assertEqual({"Agatha Christie": ["Giant's Bread"]}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
