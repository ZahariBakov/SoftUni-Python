from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(55.3, 175.6)

    def test_class_attribute(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_initialized(self):
        self.assertEqual(55.3, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(175.6, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_without_fuel_raise_exception(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(42.8, self.vehicle.fuel)

    def test_refuel_with_fuel_more_than_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_after_drive_with_correct_fuel_quantity(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(7.2)

        self.assertEqual(50, self.vehicle.fuel)

    def test_str(self):
        result = str(self.vehicle)
        expected = "The vehicle has 175.6 horse power with 55.3 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
