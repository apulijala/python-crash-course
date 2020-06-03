import unittest
from max_product import *


class MaxProduct(unittest.TestCase):
    @unittest.skip
    def test_max_product(self):
        A = [-3, 1, 2, -2, 5, 6]
        result = max_product(A)
        self.assertEqual(result, 60)
        A = [-3, 1, 2]
        result = max_product(A)
        self.assertEqual(result, -6)
        A = [-5, 5, -5, 4] 
        result = max_product(A)
        self.assertEqual(result, 125)

    def test_max_product_negative(self):
        
        A = [-3, 1, 2, -2, 5, 6]
        result = max_product_negative(A)
        self.assertEqual(result, 60)
        A = [-3, 1, 2]
        result = max_product_negative(A)
        self.assertEqual(result, -6)
        A = [-5, 5, -5, 4] 
        result = max_product_negative(A)
        self.assertEqual(result, 125)
        A = [-5, 5, -5] 
        result = max_product_negative(A)
        self.assertEqual(result, 125)
        A = [-5, 5, 5] 
        result = max_product_negative(A)
        self.assertEqual(result, -125)
        A = [-5, -5, -5] 
        result = max_product_negative(A)
        self.assertEqual(result, -125)
        A = [-5, -5, -5, 6] 
        result = max_product_negative(A)
        self.assertEqual(result, 150)
        
        A =  [-4, -6, 3, 4, 5] 
        result = max_product_negative(A)
        self.assertEqual(result, 120)


if __name__ == "__main__":
    unittest.main()