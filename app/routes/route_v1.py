from flask import Flask, jsonify, request, make_response
from services.property_service import PropertyService

class RouteV1:

    PREFIX_API = '/api/v1'

    app = Flask(__name__)

    @app.route(f'{PREFIX_API}/', methods=['GET'])
    def index():
        return RouteV1.response({'message': 'run server!'})

    @app.route(f'{PREFIX_API}/properties', methods=['GET'])
    def properties():
        property_service = PropertyService()
        return RouteV1.response(property_service.get_all())

    @app.route(f'{PREFIX_API}/properties', methods=['POST'])
    def properties_filter():
        data = request.get_json()
        property_service = PropertyService()
        return RouteV1.response(property_service.filter(data))
    
    #genera la respuesta http con los datos suministrados
    def response(data):
        message = 'success'
        code = 200

        if not data:
            message = 'Not data found'
            code = 404

        return make_response(jsonify({'data': data, 'message': message}), code)
    
    # retorna el objeto app
    def get_app(self) -> Flask:
        return self.app