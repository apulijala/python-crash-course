from frog_jump import *
from find_missing_eleemnt import *
import unittest

"""
Scored 100% and completed in 10 mins
"""

class FrogJump(unittest.TestCase):
    @unittest.skip
    def test_frog_jump(self):
        self.assertEqual(frogjump(10, 85, 30), 3)
        self.assertEqual(frogjump(10, 89, 30), 3)
        self.assertEqual(frogjump(10, 90, 30), 3)
        self.assertEqual(frogjump(10, 91, 30), 3)
        self.assertEqual(frogjump(10, 100, 30), 3)
        self.assertEqual(frogjump(0, 100, 10), 10)

    @unittest.skip
    def test_missing_element(self):
       A =  [2, 3, 1, 5]
       self.assertEqual(find_missing_element(A), 4)
       A =  [9, 8, 7, 5, 1, 2, 4, 3]
       self.assertEqual(find_missing_element(A), 6)
    @unittest.skip
    def test_missing_element_empty_or_one(self):
        A =  [2]
        result = find_missing_element(A)
        print(result)
        self.assertEqual(result, 1)
        A = []
        result = find_missing_element(A)
        print(result)
        self.assertEqual(result, 1)
        A = [2,3,4]
        result = find_missing_element(A)
        print(result)
        self.assertEqual(result, 1)
        A = [2,3,4,]
        result = find_missing_element(A)
        print(result)
        self.assertEqual(result, 1)

        A = [1] 
        result = find_missing_element(A)
        print(result)
        self.assertEqual(result, 1)
    
    def test_min_difference(self):
        A = [3, 1, 2, 4, 3] # This is an example test case. 
        self.assertEqual(min_difference(A), 1)

        A = [3, 1] # this is for least border.  with some value
        self.assertEqual(min_difference(A), 2)
        
        A = [1, 1] # This is for the least border, but with 0 value. 
        self.assertEqual(min_difference(A), 0)

        A = range(1,100000) # Just verified for large range  that it runs fast.
                            # Could not get the result. 
        min_difference(A)
        # self.assertEqual(min_difference(A), 0)

    # Started at position 21:25. Actual coding
    # start at 21:30
    def test_frog_river_one(self):
        """

        """
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        self.assertEqual(frog_river_one(5,A), 6)       
  
  

        


if __name__ == "__main__":
    unittest.main()