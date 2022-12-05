from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie("Test", 1981, 5)

    def test_correct_initialized(self):
        self.assertEqual("Test", self.movie.name)
        self.assertEqual(1981, self.movie.year)
        self.assertEqual(5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_if_name_is_empty_string_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        expected = "Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_year_before_expecting_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886

        expected = "Year is not valid!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_actors_with_new_actor(self):
        self.movie.add_actor("Sirma")
        self.assertEqual(["Sirma"], self.movie.actors)

    def test_add_actors_with_existing_actor_return_message(self):
        self.movie.add_actor("Sirma")

        result = self.movie.add_actor("Sirma")
        expected = "Sirma is already added in the list of actors!"

        self.assertEqual(expected, result)

    def test__gt__first_rating_bigger_than_other(self):
        second_movie = Movie("SecondMovie", 1981, 3)

        result = self.movie > second_movie
        expected = '"Test" is better than "SecondMovie"'

        self.assertEqual(expected, result)

    def test__gt__first_rating_lowest_than_other(self):
        second_movie = Movie("SecondMovie", 1981, 7)

        result = self.movie > second_movie
        expected = '"SecondMovie" is better than "Test"'

        self.assertEqual(expected, result)

    def test__repr_method(self):
        self.movie.add_actor("Sirma")
        self.movie.add_actor("Zahari")

        expected = "Name: Test\n" \
                   "Year of Release: 1981\n" \
                   "Rating: 5.00\n" \
                   "Cast: Sirma, Zahari"

        self.assertEqual(expected, self.movie.__repr__())


if __name__ == '__main__':
    main()
