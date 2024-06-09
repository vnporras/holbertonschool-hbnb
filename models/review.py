from hbnb import BaseHbnB
from datetime import datetime
import uuid

class Review:
  def __init__(self, user, place, content, rating):
    self.id = uuid.uuid4()
    self.user = user
    self.place = place
    self.content = content
    self.rating = rating