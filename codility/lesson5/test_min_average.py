from  min_average import *
import unittest

class MinAverage(unittest.TestCase):
        

    def test_min_average_of_slices(self):
        
        A = [4, 2, 2, 5, 1, 5, 8]
        result = min_average_of_slices(A)
        self.assertEqual(result, 1)
        A = [10000, -10000]
        result = min_average_of_slices(A)
        self.assertEqual(result, 0)
        

if __name__ == "__main__":
    unittest.main()
