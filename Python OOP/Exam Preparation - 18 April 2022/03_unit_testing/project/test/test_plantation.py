from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(5)

    def test_correct_initialized(self):
        self.assertEqual(5, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_with_negative_value_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -10

        expected = "Size must be positive number!"
        self.assertEqual(expected, str(ve.exception))

    def test_len_wrong_count(self):
        self.plantation = Plantation(1)
        self.plantation.hire_worker('Martin')
        self.plantation.plants['Martin'] = ['Tomatoes']
        self.assertEqual(self.plantation.__len__(), 1)

    def test_hire_worker_who_is_exist_raise_value_error(self):
        self.plantation.workers = ["test_worker"]

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("test_worker")

        expected = "Worker already hired!"
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual(1, len(self.plantation.workers))

    def test_hire_worker_correct(self):
        result = self.plantation.hire_worker("test_worker")
        self.assertEqual(["test_worker"], self.plantation.workers)

        expected = "test_worker successfully hired."
        self.assertEqual(expected, result)

    def test__len__method(self):
        self.plantation.plants = {"first_plant": 1, "second_plant": 2, "third_plant": 3}

        self.assertEqual(3, len(self.plantation.plants))

    def test_planting_with_invalid_workers_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("test_worker", "first_plant")

        expected = "Worker with name test_worker is not hired!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_with_invalid_len_of_name_raise_value_error(self):
        self.plantation.size = 1
        self.plantation.workers = ["first_worker"]
        self.plantation.plants = {"first_worker": "first_plant"}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("first_worker", "fourth_plant")

        expected = "The plantation is full!"
        self.assertEqual(expected, str(ve.exception))

    def test_planting_with_exist_worker(self):
        self.plantation.size = 2
        self.plantation.hire_worker('Martin')
        self.plantation.planting('Martin', 'Radishes')
        self.assertEqual(self.plantation.planting('Martin', 'Radishes'), 'Martin planted Radishes.')

    def test_planting_if_worker_plant_for_first_time(self):
        self.plantation.hire_worker("Martin")
        result = self.plantation.planting('Martin', 'Radishes')

        self.assertEqual(1, len(self.plantation.plants["Martin"]))

        expected = "Martin planted it's first Radishes."
        self.assertEqual(expected, result)

    def test__str__method_wrong_output(self):
        self.plantation.hire_worker('Martin')
        self.plantation.hire_worker('Ivan')
        self.plantation.planting('Martin', 'Radishes')
        self.plantation.planting('Martin', 'carrots')
        self.plantation.planting('Ivan', 'cucumber')
        self.plantation.planting('Ivan', 'potato')

        expected = 'Plantation size: 5\nMartin, Ivan\nMartin planted: Radishes, carrots\nIvan planted: cucumber, potato'
        self.assertEqual(expected, str(self.plantation))

    def test__repr_method(self):
        self.plantation.hire_worker('Martin')
        self.plantation.hire_worker('Ivan')

        expected = "Size: 5\nWorkers: Martin, Ivan"
        self.assertEqual(expected, repr(self.plantation))


if __name__ == '__main__':
    main()

