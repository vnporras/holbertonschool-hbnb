from data_persistence import DataPersistence

class BusinessLogic:
    @staticmethod
    def validate_email_unique(email):
        for user in DataPersistence.read_data('users'):
            if user.email == email:
                return False
        return True

    @staticmethod
    def validate_host_unique_place(host, place):
        for existing_place in DataPersistence.read_data('places'):
            if existing_place.host == host and existing_place.name == place.name:
                return False
        return True

    @staticmethod
    def process_data(data):
        return data