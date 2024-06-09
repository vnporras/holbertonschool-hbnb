from hbnb import BaseHbnB
from datetime import datetime
import uuid


class User:
  def __init__(self, email, password, first_name, last_name):
    self.id = uuid.uuid4()
    self.email = email
    self.password = password
    self.first_name = first_name
    self.last_name = last_name