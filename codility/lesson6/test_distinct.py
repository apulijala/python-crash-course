from distinct import *
import unittest

class CountDistinct(unittest.TestCase):
    def test_count_distinct(self):
        A = [2, 1, 1, 2, 3, 1]
        result = count_distinct(A)
        self.assertEqual(result, 3)

        A = []
        result = count_distinct(A)
        self.assertEqual(result, 0)

        A = [5]
        result = count_distinct(A)
        self.assertEqual(result, 1)

        A = [-2, 5, -2]
        result = count_distinct(A)
        self.assertEqual(result, 2)
        


        




if __name__ == "__main__":
    unittest.main()
