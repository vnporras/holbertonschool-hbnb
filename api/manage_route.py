from flask import Flask, request
from services_layer import ServicesLayer

app = Flask(__name__)


@app.route("/api/entity", methods=["POST", "GET", "PUT", "DELETE"])
def handle_entity():
    response = ServicesLayer.handle_requests(request)
    return ServicesLayer.handle_response(response)


if __name__ == "__main__":
    app.run(debug=True)
