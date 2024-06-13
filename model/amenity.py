from datetime import datetime
import uuid


class Amenity:
    def __init__(self, name):
        self.name = name
        self.unique_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()