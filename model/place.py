#!/usr/bin/python3
from datetime import datetime
import uuid

class Place:
    def __init__(self, name, description, address, city, latitude, longitude, host, num_rooms, num_bathrooms, price_per_night, max_guests, amenities=None):
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = amenities if amenities else []
        self.reviews = []
        self.unique_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_review(self, review):
        self.reviews.append(review)


    def add_amenity(self, amenity):
        self.amenities.append(amenity)
