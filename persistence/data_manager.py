from data_persistence import DataPersistence
from persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def save(self, entity):
        DataPersistence.write_data(entity.__class__.__name__.lower() + 's', entity)

    def get(self, entity_id, entity_type):
        entities = DataPersistence.read_data(entity_type.lower() + 's')
        for entity in entities:
            if entity.unique_id == entity_id:
                return entity
        return None

    def update(self, entity):
        existing_entity = self.get(entity.unique_id, entity.__class__.__name__)
        if existing_entity:
            index = DataPersistence.read_data(entity.__class__.__name__.lower() + 's').index(existing_entity)
            DataPersistence.read_data(entity.__class__.__name__.lower() + 's')[index] = entity

    def delete(self, entity_id, entity_type):
        DataPersistence.delete_data(entity_type.lower() + 's', entity_id)