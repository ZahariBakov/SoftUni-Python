from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Test Name", 100, 10)

    def test_worker_is_correct_initialized(self):
        self.assertEqual("Test Name", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_energy_is_increased_after_rest(self):
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_raise_exception_when_worker_is_working_with_zero_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_money_is_increased_after_working(self):
        self.worker.work()

        self.assertEqual(100, self.worker.money)

        self.worker.work()

        self.assertEqual(200, self.worker.money)

    def test_energy_is_decreased_after_work(self):
        self.worker.work()

        self.assertEqual(9, self.worker.energy)

    def test_correct_get_info(self):
        result = self.worker.get_info()
        expect = "Test Name has saved 0 money."

        self.assertEqual(expect, result)


if __name__ == '__main__':
    main()