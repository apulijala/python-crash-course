import unittest
from alien import * 

class AlienTest(unittest.TestCase):
    def test_alien_color_if(self):
        self.assertEqual(alien_color_if("Green"), 5)
        self.assertEqual(alien_color_if("green"), 5)
        self.assertEqual(alien_color_if("red"), 10)
        self.assertEqual(alien_color_if("Red"), 10)
    
    def test_alien_color_if_else_if(self):
        self.assertEqual(alien_color_if_else_if("green"), 5, "Green should return 5")
        self.assertEqual(alien_color_if_else_if("yellow"), 10, "Yellow should return 10")
        self.assertEqual(alien_color_if_else_if("Red"), 15, "Red should return 15")
        self.assertEqual(alien_color_if_else_if("blue"), 20, "Any other color should return 20")


if __name__ == "__main__":
    unittest.main()