from datetime import datetime
import uuid

class Review:
    def __init__(self, user, place, text, rating):
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
        self.unique_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()