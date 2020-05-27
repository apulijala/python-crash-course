import unittest
from city_functions import city_country


class CitiesCounty(unittest.TestCase):
    def test_city_county(self):
        city_country1 = city_country("santiago", "chile")
        self.assertEquals(city_country1, "Santiago, Chile")

    def test_city_country_population(self):
        city_country_population = city_country("santiago", "chile", 5000000)
        self.assertEquals(city_country_population, "Santiago, Chile - Population 5000000")


if __name__ == '__main__':
    unittest.main()