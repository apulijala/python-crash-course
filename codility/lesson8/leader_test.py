from leader  import *
import unittest

class LeaderTest(unittest.TestCase):
    
    def setUp(self):
        self.A = [6,8,4,6,8,6,6]

    def test_slow_leader(self):
        result = slow_leader(self.A)
        self.assertEqual(result, 6)
    
    def test_fast_leader(self):
        result = fast_leader(self.A)
        self.assertEqual(result, 6)
    
    
    def test_golden_leader(self):
        result = golden_leader(self.A)
        self.assertEqual(result, 6)
    

    def test_solution(self):
        result = solution(self.A)
        self.assertEqual(result, 0)
    
    def test_equi_leader(self):
   
        A = [4,3,4,4, 4, 2]
        result = equi_leader(A)
        self.assertEqual(result,2)

        result = equi_leader(A)
        self.assertEqual(result,2)
   
   
        A = [4,3]
        result = equi_leader(A)
        self.assertEqual(result,0)



    
        
    


if __name__ == "__main__":
    unittest.main()