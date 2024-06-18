#!/usr/bin/python3
import unittest
from datetime import datetime
from unittest.mock import patch
import uuid
from model.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_name_initialization(self):
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")
    
    def test_unique_id_generation(self):
        amenity = Amenity(name="Gym")
        self.assertIsInstance(amenity.unique_id, str)
        self.assertTrue(uuid.UUID(amenity.unique_id))

    @patch('model.amenity.datetime')
    def test_created_at_initialization(self, mock_datetime):
        now = datetime(2024, 6, 13)
        mock_datetime.now.return_value = now
        amenity = Amenity(name="Sauna")
        self.assertEqual(amenity.created_at, now)
        self.assertEqual(amenity.updated_at, now)
    
    def test_updated_at_initialization(self):
        amenity = Amenity(name="WiFi")
        self.assertTrue(isinstance(amenity.updated_at, datetime))
    
    def test_unique_id_uniqueness(self):
        amenity1 = Amenity(name="Gym")
        amenity2 = Amenity(name="Pool")
        self.assertNotEqual(amenity1.unique_id, amenity2.unique_id)

if __name__ == '__main__':
    unittest.main()
