from queue import *
import unittest

class QueueTest(unittest.TestCase):
    def setUp(self):
        self.my_queue = Stack()
    
    @unittest.skip
    def test_queue(self):
        # A = [0, 1]
        # B = [1, 1]
        self.my_queue.push(101)
        self.my_queue.push(100)
        self.assertEqual(self.my_queue.size(), 2)
        
        self.my_queue = Queue(2)
        self.my_queue.push(100)
        self.my_queue.push(101)
        self.my_queue.push(102)

        result = self.my_queue.pop()
        self.assertEqual(result, 100)
        self.assertFalse(self.my_queue.empty())

        result = self.my_queue.pop()
        self.assertEqual(result, 101)

        result = self.my_queue.pop()
        self.assertEqual(result, 102)

        self.assertTrue(self.my_queue.empty())
        result = self.my_queue.pop()
        self.assertNotEqual(result, 102)


    # @unittest.skip
    def test_fish_attack(self):

        
        A = [4, 3, 2, 1, 5]
        B = [0, 1, 0, 0, 0]
        result = fish_attack(A, B)
        self.assertEqual(result, 2)
        

        A = [4]
        B = [0]
        result = fish_attack(A, B)
        self.assertEqual(result, 1)

        A = [4]
        B = [1]
        result = fish_attack(A, B)
        self.assertEqual(result, 1)
        

        A = [4, 3, 2, 6, 5]
        B = [0, 1, 0, 1, 0]
        result = fish_attack(A, B)
        self.assertEqual(result, 3)
        
        A = [4, 3, 2, 6, 5, 4]
        B = [0, 1, 0, 1, 0, 0]
        result = fish_attack(A, B)
        self.assertEqual(result, 3)
        
        A = [4, 3, 2, 6, 5, 8]
        B = [0, 1, 0, 1, 0, 0]
        result = fish_attack(A, B)
        self.assertEqual(result, 2)
        
        A = [4, 3, 2, 6, 5, 8]
        B = [0, 1, 0, 1, 0, 1]
        result = fish_attack(A, B)
        self.assertEqual(result, 4)
        
        A = [0, 1]
        B = [1, 1]
        result = fish_attack(A, B)
        self.assertEqual(result, 2)
        

        A = [10,9,8,7,6,5]
        B = [1,0,0,0,0,0]
        result = fish_attack(A, B)
        self.assertEqual(result, 1)
        
        A = [10,9,8,7,6,5,4]
        B = [1,0,0,0,0,0,1]
        result = fish_attack(A, B)
        self.assertEqual(result, 2)
        

if __name__ == "__main__":
    unittest.main()