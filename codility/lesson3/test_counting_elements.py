import unittest
from counting_elements import *


class CountingElements(unittest.TestCase):
    @unittest.skip
    def test_count_elements(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        count_elements(A, 5)

    @unittest.skip
    def test_frog_jump(self):
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        self.assertEqual(frog_jump(5,A), 6)
        A = [1,  1, 4, 2, 5, 4]
        self.assertEqual(frog_jump(5,A),-1)
        A = [1]
        self.assertEqual(frog_jump(1,A), 0)
        A = [2]
        self.assertEqual(frog_jump(1,A), -1)
        print(frog_jump(100000,list(range(1,100001))))

    """
        Started at 15:49 - finished 
        understanding in 15:59
        carys thomas, 22 Sep 1999, 5:00 AM
        +35 mins
    """
    @unittest.skip
    def test_counters(self):
        A = [3, 4, 4, 6, 1, 4, 4]
        result = counter(5, A)
        self.assertListEqual(result, [3, 2, 2, 4, 2])

    """
        16:32 second attempt
    """
    def test_counters_again(self):
        A = [3, 4, 4, 6, 1, 4, 4]
        result = counter_again(5, A)
        self.assertListEqual(result, [3, 2, 2, 4, 2])



        
if __name__ == "__main__":
    unittest.main()