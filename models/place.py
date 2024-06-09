from hbnb import BaseHbnB
from datetime import datetime
import uuid

class Place:
  def __init__(self, name, description, address, city, latitude, longitude, number_rooms, bathrooms, price_per_night, max_guests):
    self.id = uuid.uuid4()
    self.name = name
    self.description = description
    self.address = address
    self.city = city
    self.latitude = latitude
    self.longitude = longitude
    self.number_rooms = number_rooms
    self.bathrooms = bathrooms
    self.price_per_night = price_per_night
