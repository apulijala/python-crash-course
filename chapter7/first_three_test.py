import unittest
from first_three import *

class FirstThree(unittest.TestCase):

    @unittest.skip
    def test_rental_car(self):
        rental_car()

    def test_restaurant(self):
        print("\n")
        print(restaurant(8))
        self.assertEqual(restaurant(8), "Table is ready")
        print(restaurant(7))
        self.assertEqual(restaurant(7), "Table is ready")
        print(restaurant(9))
        self.assertEqual(restaurant(9), "You'll have to wait for the table")

    def test_multiples_of_ten(self):
        self.assertTrue(multiples_of_ten(10))
        self.assertTrue(multiples_of_ten(100))
        self.assertFalse(multiples_of_ten(9))
        self.assertFalse(multiples_of_ten(99))

        num = int(input("Please enter a number ? "))
        if multiples_of_ten(num):
            print(f"{num} is a multiple of 10")
        else: 
            print(f"{num} is not a  multiple of 10")





if __name__ == "__main__":
    unittest.main()