from frog_jump import *
import unittest

"""
Scored 100% and completed in 10 mins
"""

class FrogJump(unittest.TestCase):
    def test_frog_jump(self):
        self.assertEqual(frogjump(10, 85, 30), 3)
        self.assertEqual(frogjump(10, 89, 30), 3)
        self.assertEqual(frogjump(10, 90, 30), 3)
        self.assertEqual(frogjump(10, 91, 30), 3)
        self.assertEqual(frogjump(10, 100, 30), 3)
        self.assertEqual(frogjump(0, 100, 10), 10)


if __name__ == "__main__":
    unittest.main()