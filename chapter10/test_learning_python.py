import unittest
from learning_python import *

class LearningPythonTest(unittest.TestCase):
    def setUp(self):
        self.existing_file = "learning_python.txt"
        self.no_file = "learning_python_not_found.txt"


    def test_read_entire_file_not_existing(self):
        result = read_entire_file(self.no_file)
        self.assertEqual(result, f"{self.no_file} Not Found")

    def test_read_entire_file_exists(self):
        result = read_entire_file(self.existing_file)
        self.assertRegex(result, "Python")
        print("\nText reading entire lines")
        print(result)

    def test_read_by_storing_lines_file_no_found(self):
        result = read_by_storing_lines(self.no_file)
        self.assertEqual(result, f"{self.no_file} Not Found")


    def test_read_by_storing_lines(self):
        print("\nText reading by storing lines")
        result = read_by_storing_lines(self.existing_file)
        self.assertRegex(result, "Python")
        print(result)

    def test_read_by_looping_over_file(self):
        print("\nText reading by looping over file")
        result = read_by_storing_lines(self.existing_file)
        self.assertRegex(result, "Python")
        self.assertNotRegex(result, r"^$")
        print(result)

if __name__ == "__main__":
    unittest.main()