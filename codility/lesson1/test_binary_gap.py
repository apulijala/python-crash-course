import unittest
from binary_gap import *

class BinaryGaptest(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(1162), 3)
        self.assertEqual(solution(51712), 2)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)
     
        
        


    @unittest.skip
    def test_get_binary_string_from_num(self):
        result = get_binary_string_from_num(5)
        print(result)
        result = get_binary_string_from_num(1)
        print(result)
        result = get_binary_string_from_num(529)
        print(result)

if __name__ == "__main__":
    unittest.main()