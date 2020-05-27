import unittest
from person import *


class PersonTest(unittest.TestCase):
    def test_person(self):
        result = person("arvind", "pulijala", 45, "llandysul")
        self.assertEqual(result['first_name'], "Arvind")
        self.assertEqual(result['last_name'], "Pulijala")
        self.assertEqual(result['age'], 45)
        self.assertEqual(result['city'], "Llandysul")

    def test_person_empty_vals(self):
        result = person(" ", "", 45, "llandysul")
        self.assertEqual(result['first_name'], " ")
        self.assertEqual(result['last_name'], "")
        self.assertEqual(result['age'], 45)
        self.assertEqual(result['city'], "Llandysul")
    
    def test_favorite_numes(self):
        favorite_numes()
    
    def test_glooserY(self):
        glossary()
    
    def test_persons_list(self):
        persons = person_list("Latifa", "Whore", 31, "London")
        print("\n")   
        for person in persons:
            print("==========")
            print(f"First Name  = {person['first_name'].title()} ")
            print(f"Last Name  = {person['last_name'].title()} ")
            print(f"Age  = {person['age']}")
            print(f"City  = {person['city']}")
            


# print(__name__)

if __name__ == "__main__":
    unittest.main()
