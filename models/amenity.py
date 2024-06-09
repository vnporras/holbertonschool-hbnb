from hbnb import BaseHbnB
from datetime import datetime
import uuid


class Amenity:
  def __init__(self, name):
    self.id = uuid.uuid4()
    self.name = name