from flask import Flask, jsonify, request, make_response
from services.property_service import PropertyService

class Route:

    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return Route.response({'message': 'run server!'})

    @app.route('/properties', methods=['GET'])
    def properties():
        property_service = PropertyService()
        return Route.response(property_service.get_all())

    @app.route('/properties', methods=['POST'])
    def properties_filter():
        data = request.get_json()
        property_service = PropertyService()
        return Route.response(property_service.filter(data))
    
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