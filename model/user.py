from datetime import datetime
import uuid


class User:
    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.hosted_places = []
        self.written_reviews = []
        self.unique_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def authenticate(self, email, password):
        pass

    def manage_hosted_places(self):
        pass

    def write_reviews(self):
        pass