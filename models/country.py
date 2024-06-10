from hbnb import BaseHbnB
from datatime import datetime
import uuid

class country:
    def __init__(self, name, country):
        self.id = uuid.uuid4()
        self.name = name
        self.country = country