import unittest
from pets import *

class PetsTest(unittest.TestCase):
    def test_pets(self):
        pets()

    def test_favorite_places(self):
        favorite_places()

    def test_cities(self):
        cities_info()


if __name__ == "__main__":
    unittest.main()