from flask import Flask, jsonify, request, make_response
from routes.route import Route
from services.property_service import PropertyService

class RouteV1(Route):

    PREFIX_API = '/api/v1'

    app = Flask(__name__)

    @app.route(f'{PREFIX_API}/', methods=['GET'])
    def index():
        return Route.response({'message': 'run server!'})

    @app.route(f'{PREFIX_API}/properties', methods=['GET'])
    def properties():
        property_service = PropertyService()
        return Route.response(property_service.get_all())

    @app.route(f'{PREFIX_API}/properties', methods=['POST'])
    def properties_filter():
        data = request.get_json()
        property_service = PropertyService()
        return Route.response(property_service.filter(data))