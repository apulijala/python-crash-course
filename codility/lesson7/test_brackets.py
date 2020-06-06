import unittest
from brackets import *
from fish_direction import *

class Brackets(unittest.TestCase):
    def test_brackets(self):
        
        my_str = ""
        result = brackets(my_str)
        self.assertEqual(result, 1)

        my_str = "{[()()]}"
        result = brackets(my_str)
        self.assertEqual(result, 1)     

        my_str = "{[()[]]}"
        result = brackets(my_str)
        self.assertEqual(result, 1)

        my_str = "([)()]"
        result = brackets(my_str)
        self.assertEqual(result, 0)

        my_str = "([)()]"
        result = brackets(my_str)
        self.assertEqual(result, 0)

        my_str = "')('"
        result = brackets(my_str)
        self.assertEqual(result, 0)

        my_str = "{{{{"
        result = brackets(my_str)
        self.assertEqual(result, 0)

    def test_brackets_only_one_type(self):
        
        my_str = ""
        result = brackets(my_str)
        self.assertEqual(result, 1)

        my_str = "(()(())())" 
        result = brackets(my_str)
        self.assertEqual(result, 1)     

        my_str = "())"
        result = brackets(my_str)
        self.assertEqual(result, 0)

    def test_fish_and_moments(self):
        A = [4, 3, 2, 1, 5]
        B = [0, 1, 0, 0, 0]
        result = fish_and_moments(A,B)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
    