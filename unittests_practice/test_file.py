import unittest
import sys
sys.path.append('../')
from unittests_practice.file import Car, IllegalCarError


class TestFile(unittest.TestCase):

    def test_total_mass(self):
        car_one = Car(2, 40, 5)
        self.assertEqual(car_one.total_mass, 180)

    def test_pax_count_empty_car(self):
        with self.assertRaises(IllegalCarError) as context:
            Car(0, 40, 5).pax_count()
        self.assertTrue("No passengers" in str(context.exception))

    def test_pax_count_to_many(self):
        with self.assertRaises(IllegalCarError) as context:
            Car(6, 1500, 6).pax_count()
        self.assertTrue("To many passengers" in str(context.exception))

    def test_car_mass_to_heavy(self):
        with self.assertRaises(IllegalCarError) as context:
            Car(5, 2100, 6).car_mass()
        self.assertTrue("Car is to heavy" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
