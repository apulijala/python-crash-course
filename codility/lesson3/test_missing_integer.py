import unittest
from missing_integer import *

class MissingInteger(unittest.TestCase):

    
    def test_missing_integer(self):
        A =  [-1, -3]
        result = missing_integer(A)
        self.assertEqual(result,1)
        A = [1, 3, 6, 4, 1, 2]
        result = missing_integer(A)
        self.assertEqual(result, 5)
        A = [1, 3, 6, 4, 1, -3, -5, 2]
        result = missing_integer(A)
        self.assertEqual(result, 5)
        A = [1, 3, 2]
        result = missing_integer(A)
        self.assertEqual(result, 4)
        A = list(range(1, 100000))
        del A[999]
        result = missing_integer(A)
        self.assertEqual(result, 1000)
        A = list(range(-100000, 100000))
        del A[100999]
        self.assertEqual(result, 1000)
    
    def test_permutation(self):
        A = [4, 1, 3, 2]
        result = permutation(A)
        self.assertEqual(result,1 )
        A = [4, 2, 1]
        result = permutation(A)
        self.assertEqual(result,0)
        A = [4, 2, 1]
        result = permutation(A)
        self.assertEqual(result,0)
        A =  [4, 1, 3,1, 2]
        result = permutation(A)
        self.assertEqual(result,0)

        A =  [4]
        result = permutation(A)
        self.assertEqual(result,0)

        A =  [1]
        result = permutation(A)
        self.assertEqual(result,1)

        A =  [1000000]
        result = permutation(A)
        self.assertEqual(result,0)

        


if __name__ == "__main__":
    unittest.main()        
