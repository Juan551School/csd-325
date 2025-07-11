# Juan Macias Vasquez
# Date 06/27/2025
# Module 7.2
# test_cities.py

import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()

