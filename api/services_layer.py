import json

class ServicesLayer:
    @staticmethod
    def handle_requests(request):
        # Analizamos la solicitud JSON que se ingresa
        request_data = json.loads(request)
        
        # Estraemos el tipo de solicitud y los datos
        request_type = request_data.get("type")
        data = request_data.get("data")
        
        # Inicializamos la respuesta
        response = {"status": "error", "message": "Invalid request"}
        
        # Procesamos la solicitud en funcion del tipo
        if request_type == "GET_ALL_USERS":
            # Logica para conseguir todos los usuarios
            users = get_all_users()
            response = {"status": "success", "data": users}
        elif request_type == "GET_USER":
            # Logica para obtener un usuario especifico por ID
            user_id = data.get("id")
            user = get_user_by_id(user_id)
            if user:
                response = {"status": "success", "data": user}
            else:
                response = {"status": "error", "message": "User not found"}
        elif request_type == "CREATE_USER":
            # Logica para crear usuarios nuevos
            user_data = data
            new_user = create_user(user_data)
            response = {"status": "success", "data": new_user}
        elif request_type == "UPDATE_USER":
            # Logica para actualizar usuario especifico
            user_id = data.get("id")
            updated_data = data.get("data")
            updated_user = update_user(user_id, updated_data)
            if updated_user:
                response = {"status": "success", "data": updated_user}
            else:
                response = {"status": "error", "message": "User not found or update failed"}
        elif request_type == "DELETE_USER":
            # Logica para eliminar un usuario especifico
            user_id = data.get("id")
            if delete_user(user_id):
                response = {"status": "success", "message": "User deleted successfully"}
            else:
                response = {"status": "error", "message": "User not found or deletion failed"}
        
        # Retorno de los datos respuesta
        return response

    @staticmethod
    def handle_responses(response):
        # Format the response data into JSON
        response_data = json.dumps(response)
        
        # Return the JSON-formatted response
        return response_data

# Example utility functions (implement these according to your database or storage logic)
def get_all_users():
    # Dummy data, replace with actual logic
    return [
        {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
        {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com"}
    ]

def get_user_by_id(user_id):
    # Dummy data, replace with actual logic
    if user_id == 1:
        return {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
    else:
        return None

def create_user(user_data):
    # Dummy data, replace with actual logic
    return {"id": 3, "name": user_data["name"], "email": user_data["email"]}

def update_user(user_id, updated_data):
    # Dummy data, replace with actual logic
    if user_id == 1:
        return {"id": 1, "name": updated_data["name"], "email": updated_data["email"]}
    else:
        return None

def delete_user(user_id):
    # Dummy data, replace with actual logic
    if user_id == 1:
        return True
    else:
        return False