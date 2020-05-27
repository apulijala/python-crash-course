import unittest
from stages_of_life import *


class StagesOfLife(unittest.TestCase):
    def test_stages_of_life(self):
        print("Testing Baby and Tooddler")
        print(stages_of_life(1))
        self.assertEqual(stages_of_life(1), "baby")
        print(stages_of_life(2))
        print(stages_of_life(3))
        self.assertEqual(stages_of_life(2), "toddler")
        self.assertEqual(stages_of_life(3), "toddler")


    def test_stages_of_life_kid_teenager(self):
        print("\nTesting Kid and Teenager")
        print(stages_of_life(4))
        self.assertEqual(stages_of_life(4), "kid")
        print(stages_of_life(5))
        self.assertEqual(stages_of_life(5), "kid")
        print(stages_of_life(13))
        self.assertEqual(stages_of_life(13), "teenager")
        print(stages_of_life(14))
        self.assertEqual(stages_of_life(13), "teenager")
        print(stages_of_life(15))
        self.assertEqual(stages_of_life(13), "teenager")
        print(stages_of_life(20))
        self.assertEqual(stages_of_life(29), "adult")
        print(stages_of_life(20))
        self.assertEqual(stages_of_life(29), "adult")
    
    def test_stages_of_life_elder_adult(self):
        print("\n Testing Elder and Adult")
        print(stages_of_life(20))
        self.assertEqual(stages_of_life(20), "adult")
        print(stages_of_life(64))
        self.assertEqual(stages_of_life(64), "adult")
        self.assertEqual(stages_of_life(43), "adult")
        print(stages_of_life(43))
        self.assertEqual(stages_of_life(43), "adult")
        print(stages_of_life(65))
        self.assertEqual(stages_of_life(65), "elder")
        print(stages_of_life(70))
        self.assertEqual(stages_of_life(70), "elder")

    def test_favorite_fruits(self):
        self.assertTrue(favorite_fruits("Bananas"))
        self.assertTrue(favorite_fruits("bananas"))
        self.assertFalse(favorite_fruits("cherries"))
        self.assertFalse(favorite_fruits("Cherries"))
        fruit = "bananas"
        fruit = "Cherries"
        if favorite_fruits(fruit):
            print(f"You really like {fruit}")
        else:
            print(f"{fruit} is not your favorite fruit")


if __name__ == "__main__":
    unittest.main()