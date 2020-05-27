# 12:29
import unittest
from rotate import *

class RotateTest(unittest.TestCase):
    def test_solution(self):
        orig = [3, 8, 9, 7, 6]
        print("original array ", orig)
        result = solution(orig, 3)
        print("result is ", result)
        
        # [9, 7, 6, 3, 8]
    def test_solution_one(self):
        orig = [1, 2, 3, 4]
        print("original array ", orig)
        result = solution(orig, 4)
        print("result is ", result)

    def test_solution_two(self):
        orig = [0, 0, 0]
        print("original array ", orig)
        result = solution(orig, 1)
        print("result is ", result)

    def test_solution_three(self):
        orig = []
        print("original array ", orig)
        result = solution(orig, 4)
        print("result is ", result)

    def test_solution_four(self):
        orig = [100]
        print("original array ", orig)
        result = solution(orig, 4)
        print("result is ", result)


if __name__ == "__main__":
    unittest.main()