import unittest
from passing_cars import *

class PassingCars(unittest.TestCase):
    def test_passing_cars(self):
        A = [0, 1, 0, 1, 1]
        result = passing_cars(A)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()