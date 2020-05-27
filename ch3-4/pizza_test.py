import unittest
from pizza import *


class PizzaTest(unittest.TestCase):
    def test_pizzas(self):
        pizzas()

    def test_pets(self):
        pets()

    def test_ounting_to_twenty(self):
        counting_to_twenty()
    
    def test_million_nums(self):
        million_nums()

    def test_threes(self):
        threes()

    def test_cubes_using_for_loop(self):
        cubes_using_for_loop()

    def test_cubes_using_for_comprehension(self):
        cubes_using_for_comprehension()

    def test_pizzas_deep_copy(self):
        pizzas_deep_copy()

if __name__ == "__main__":
    unittest.main()