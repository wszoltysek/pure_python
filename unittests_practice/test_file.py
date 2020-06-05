import unittest
import sys

sys.path.append("../")
from unittests_practice.file import Car, IllegalCarError


class TestFile(unittest.TestCase):

    def test_car_total_mass(self):
        first_car = Car(2, 900, 5).total_mass
        second_car = Car(5, 1200, 5).total_mass
        third_car = Car(4, 1400, 6).total_mass
        self.assertEqual(first_car, 1040)
        self.assertEqual(second_car, 1550)
        self.assertEqual(third_car, 1680)

    def test_car_mass_to_heavy(self):
        with self.assertRaises(IllegalCarError) as context:
            Car(5, 2100, 6).car_mass()
        self.assertTrue("Car is to heavy" in str(context.exception))

    def test_pax_count_empty(self):
        with self.assertRaises(IllegalCarError) as context:
            Car(0, 40, 5).pax_count()
        self.assertTrue("No passengers" in str(context.exception))

    def test_pax_count_to_many(self):
        with self.assertRaises(IllegalCarError) as context:
            Car(6, 1500, 6).pax_count()
        self.assertTrue("To many passengers" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
