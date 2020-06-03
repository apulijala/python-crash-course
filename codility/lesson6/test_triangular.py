from triangle import *
import unittest

class TestTriangular(unittest.TestCase):

    def test_is_triangular(self):
        A = [10, 2, 5, 1, 8, 20]
        result = is_triangular(A)
        self.assertEqual(result, 1)

        A = [10, 50, 5, 1]
        result = is_triangular(A)
        self.assertEqual(result, 0)



if __name__ == "__main__":
    unittest.main()