from data_persistence import DataPersistence

class BusinessLogic:
    @staticmethod
    def validate_email_unique(email):
        for user in DataPersistence.read_data('users'):
            if user.email == email:
                return False
        return True

    @staticmethod
    def validate_host_unique_place(host):
        for places in DataPersistence.read_data('places'):
            if places.host == host:
                return False
        return True
    

    @staticmethod
    def process_data(data):
        return data
    
