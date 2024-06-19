import unittest
from datetime import datetime
from unittest.mock import patch
import uuid
from model.city import City


class TestCity(unittest.TestCase):

    def test_init(self):
        city = City("Madrid", "España")
        self.assertEqual(city.name, "Madrid")
        self.assertEqual(city.country, "España")
        self.assertIsInstance(city.places, list)
        self.assertEqual(len(city.places), 0)
        self.assertIsInstance(city.unique_id, str)
        self.assertTrue(uuid.UUID(city.unique_id).version == 4)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertEqual(city.created_at.replace(microsecond=0), city.updated_at.replace(microsecond=0))

    def test_add_place(self):
        city = City("London", "UK")
        place_name = "Big Ben"
        city.add_place(place_name)
        self.assertEqual(len(city.places), 1)
        self.assertEqual(city.places[0], place_name)
        self.assertNotEqual(city.created_at, city.updated_at)

if __name__ == "__main__":
    unittest.main()