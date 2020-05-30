import unittest
from odd_integers import *

class TestOddIntegers(unittest.TestCase):
    def test_solution(self):
        A = [9,3,9,3,9,7,9]
        result = solution(A)
        self.assertEqual(result, 7)
        A = [9,3,9,3,9,7,7,9,9]
        result = solution(A)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()