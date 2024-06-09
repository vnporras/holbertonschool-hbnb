from hbnb import BaseHbnB 
from datetime import datetime
import uuid


class City:
  def __init__(self, name, country):
    self.id = uuid.uuid4()
    self.name = name
    self.country = country