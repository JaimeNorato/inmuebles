from flask import Flask, jsonify, request, make_response
from services.property_service import PropertyService

class Route:

    app: Flask
    
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