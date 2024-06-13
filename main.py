from model import User, Place, City, Country, Amenity, Review
from api.services_layer import ServicesLayer
from persistence.data_persistence import DataPersistence
from persistence.business_logic import BusinessLogic

def main():
    # Example usage
    try:
        user1 = User(email="test1@example.com", password="pass123", first_name="John", last_name="Doe")
        user2 = User(email="test2@example.com", password="pass456", first_name="Jane", last_name="Smith")

        city = City(name="San Francisco", country="USA")
        place = Place(name="Cozy Apartment", description="A nice cozy apartment", address="123 Main St", city=city, latitude=37.7749, longitude=-122.4194, host=user1, num_rooms=2, num_bathrooms=1, price_per_night=150, max_guests=4)
        
        review = Review(user=user2, place=place, text="Great place!", rating=5)
        place.add_review(review)

        amenity = Amenity(name="WiFi")
        place.add_amenity(amenity)

        DataPersistence.write_data('places', place)
        print("Data saved successfully.")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()