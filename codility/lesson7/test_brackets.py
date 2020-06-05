import unittest
from brackets import *

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




if __name__ == "__main__":
    unittest.main()
    