class DataPersistence:
    users = []
    places = []
    reviews = []

    @staticmethod
    def read_data(data_type):
        if data_type == 'users':
            return DataPersistence.users
        elif data_type == 'places':
            return DataPersistence.places
        elif data_type == 'reviews':
            return DataPersistence.reviews
        return None

    @staticmethod
    def write_data(data_type, data):
        if data_type == 'users':
            DataPersistence.users.append(data)
        elif data_type == 'places':
            DataPersistence.places.append(data)
        elif data_type == 'reviews':
            DataPersistence.reviews.append(data)

    @staticmethod
    def delete_data(data_type, unique_id):
        if data_type == 'users':
            DataPersistence.users = [user for user in DataPersistence.users if user.unique_id != unique_id]
        elif data_type == 'places':
            DataPersistence.places = [place for place in DataPersistence.places if place.unique_id != unique_id]
        elif data_type == 'reviews':
            DataPersistence.reviews = [review for review in DataPersistence.reviews if review.unique_id != unique_id]