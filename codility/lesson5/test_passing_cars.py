import unittest
from passing_cars import *

class PassingCars(unittest.TestCase):
    @unittest.skip
    def test_passing_cars(self):
        A = [0, 1, 0, 1, 1]
        result = passing_cars(A)
        self.assertEqual(result, 5)
    
    def test_passing_cars_effecient(self):
        A = [0, 1, 0, 1, 1]
        result = passing_cars_effecient(A)
        self.assertEqual(result, 5)
    
    def test_passing_cars_for_effecient(self):
        A = [0, 1, 0, 1, 1]
        result = passing_cars_for_effecient(A)
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()