import unittest
from locations import *

class LocationTest(unittest.TestCase):
    def test_locations(self):
        places_to_visit()

    def test_places_to_visit_using_sorted(self):
        places_to_visit_using_sorted()

    def test_places_to_visit_using_sorted(self):
        places_to_visit_reversed()

    def test_places_to_visit_using_sort(self):
        places_to_visit_using_sort()
    

if  __name__ == "__main__":
    unittest.main()