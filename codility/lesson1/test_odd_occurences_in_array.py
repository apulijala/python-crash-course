import unittest
from odd_occurences_in_array import *

class TestOddOccurences(unittest.TestCase):
    def test_solution(self):
        array = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(solution(array), 7)
        array = [9, 3, 9, 3, 9, 9, 9]
        self.assertEqual(solution(array), 9)


if __name__ == "__main__":
    unittest.main()