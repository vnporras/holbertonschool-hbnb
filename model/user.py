#!/usr/bin/python3
import uuid
import re
from datetime import datetime
from persistence.data_persistence import DataPersistence
from persistence.business_logic import BusinessLogic
from review import Review


class User:
    def __init__(self, email, password, first_name, last_name):
        if not BusinessLogic.validate_email_unique(email):
            raise ValueError("Email already exists")
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.hosted_places = []
        self.written_reviews = []
        self.unique_id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        DataPersistence.write_data("users", self)

    def create_at(self, email, password, first_name, last_name):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        return self

    def update_at(
        self, new_email=None, new_password=None, new_first_name=None, new_last_name=None
    ):
        if new_email is not None:
            self.email = new_email
        if new_password is not None:
            self.password = new_password
        if new_first_name is not None:
            self.first_name = new_first_name
        if new_last_name is not None:
            self.last_name = new_last_name
        self.updated_at = datetime.now()
        return self

    def authenticate(self, email, password):
        if self.email == email and self.password == password:
            return True
        return False

    def manage_hosted_places(self):
        return self.hosted_places

    def write_review(self, place, text, rating):
        review = Review(self, place, text, rating)
        self.written_reviews.append(review)
        place.add_review(review)
        self.updated_at = datetime.now()
        DataPersistence.write_data("reviews", review)

    def is_valid_email(self):
        regex = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        return re.search(regex, self.email) is not None
