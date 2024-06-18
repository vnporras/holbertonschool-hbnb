from flask import jsonify, request
from persistence.data_manager import DataManager
from model.user import User
from model.place import Place
from model.city import City
from model.country import Country
from model.state import State
from model.amenity import Amenity
from model.review import Review

data_manager = DataManager()

class ServicesLayer:
    @staticmethod
    def handle_requests(request):
        if request.method == 'POST':
            return ServicesLayer.create_entity(request)
        elif request.method == 'GET':
            return ServicesLayer.read_entity(request)
        elif request.method == 'PUT':
            return ServicesLayer.update_entity(request)
        elif request.method == 'DELETE':
            return ServicesLayer.delete_entity(request)
        return jsonify({'message': 'Invalid request method'}), 400

    @staticmethod
    def handle_response(response):
        return jsonify(response)

    @staticmethod
    def create_entity(request):
        data = request.json
        entity_type = data.get('entity_type')
        entity_data = data.get('entity_data')

        if entity_type == 'user':
            entity = User(**entity_data)
        elif entity_type == 'place':
            entity = Place(**entity_data)
        elif entity_type == 'city':
            entity = City(**entity_data)
        elif entity_type == 'country':
            entity = Country(**entity_data)
        elif entity_type == 'state':
            entity = State(**entity_data)
        elif entity_type == 'amenity':
            entity = Amenity(**entity_data)
        elif entity_type == 'review':
            entity = Review(**entity_data)
        else:
            return jsonify({'message': 'Invalid entity type'}), 400

        data_manager.save(entity)
        return jsonify({'message': f'{entity_type.capitalize()} created successfully', 'entity': entity.__dict__}), 201

    @staticmethod
    def read_entity(request):
        entity_id = request.args.get('id')
        entity_type = request.args.get('type')
        
        if not entity_id or not entity_type:
            return jsonify({'message': 'Missing parameters'}), 400

        entity = data_manager.get(entity_id, entity_type)
        if entity:
            return jsonify(entity.__dict__), 200
        return jsonify({'message': f'{entity_type.capitalize()} not found'}), 404

    @staticmethod
    def update_entity(request):
        data = request.json
        entity_id = data.get('id')
        entity_type = data.get('type')
        entity_data = data.get('data')
        
        entity = data_manager.get(entity_id, entity_type)
        if not entity:
            return jsonify({'message': f'{entity_type.capitalize()} not found'}), 404
        
        for key, value in entity_data.items():
            setattr(entity, key, value)
        entity.updated_at = datetime.now()
        
        data_manager.update(entity)
        return jsonify({'message': f'{entity_type.capitalize()} updated successfully', 'entity': entity.__dict__}), 200

    @staticmethod
    def delete_entity(request):
        entity_id = request.args.get('id')
        entity_type = request.args.get('type')
        
        if not entity_id or not entity_type:
            return jsonify({'message': 'Missing parameters'}), 400

        entity = data_manager.get(entity_id, entity_type)
        if not entity:
            return jsonify({'message': f'{entity_type.capitalize()} not found'}), 404
        
        data_manager.delete(entity_id, entity_type)
        return jsonify({'message': f'{entity_type.capitalize()} deleted successfully'}), 200