from verify_user import *
import unittest
import os.path as path
import os

class TestVerifyUser(unittest.TestCase):
    def test_store_user(self):
        filename = "users.json"
        if path.isfile(filename):
            print("File name exists")
            os.remove(filename) # so that the test starts clean.
            
        favNum = get_fav_num(filename, "Andrew") 
        self.assertIsNone(favNum)

        store_fav_num(filename, "Andrew", 5)
        favNum = get_fav_num(filename, "Andrew")
        print(favNum)
        self.assertEqual(favNum, 5)



if __name__ == "__main__":
    unittest.main()