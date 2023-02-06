from flask import Flask, jsonify, request, make_response
from flasgger import Swagger, fields
from routes.route import Route
from services.property_service import PropertyService


class RouteV1(Route):

    PREFIX_API = '/api/v1'

    app = Flask(__name__)
    swagger = Swagger(app)

    @app.route(f'{PREFIX_API}/', methods=['GET'])
    def index():
        """
        Varifica si el servidor esta corriendo
        ---
        responses:
            200:
                data: data
                description: status del servidor
                schema:
                    id: status_server
                    properties:
                        data:
                            type: object
                            description: respuesta del servidor
                            properties:
                                message:
                                    type: string
                                    description: mensaje de verificacion
                                    default: run server!
                        message:
                            type: string
                            description: status de la peticion
                            default: success                       
        """
        
        return Route.response({'message': 'run server!'})

    @app.route(f'{PREFIX_API}/properties', methods=['GET'])
    def properties():
        """
        Obtiene el listado de inmuebles con status pre_venta”, “en_venta” y “vendido”
        ---
        responses:
            200:
                data: properties
                description: listado de inmuebles
                schema:
                    id: data_properties_all
                    properties:
                        data:
                            type: array
                            description: listado de inmuebles
                            items:
                                type: object
                                properties:
                                    id:
                                        type: integer
                                        description: id del inmueble
                                        default: 1
                                    description:
                                        type: string
                                        description: descripcion del inmueble
                                        default: Hermoso apartamento...
                                    status:
                                        type: string
                                        description: estado del inmueble
                                        default: en_venta
                                    city:
                                        type: string
                                        description: ciudad del inmueble
                                        default: bogota
                                    address:
                                        type: string
                                        description: direccion del inmueble
                                        default: cra 1 # 2 - 3
                                    price:
                                        type: integer
                                        description: precio del inmueble
                                        default: 1000000
                                    year:
                                        type: integer
                                        description: año de construccion del inmueble
                                        default: 2010
                        message:
                            type: string
                            description: status de la peticion
                            default: success

        """
        property_service = PropertyService()
        return Route.response(property_service.get_all())

    @app.route(f'{PREFIX_API}/properties', methods=['POST'])
    def properties_filter():
        """
        Obtiene el listado de inmuebles con filtrados por status (“pre_venta”, “en_venta” y “vendido”) por ciudad y/o año de construcción
        ---
        parameters:
            - name: filters
              in: query
              required: true
              schema:
                id: filters
                properties:
                    status:
                        type: string
                        description: estado del inmueble
                        default: en_venta
                    city:
                        type: string
                        description: ciudad del inmueble
                        default: bogota
                    year:
                        type: integer
                        description: año de construccion del inmueble
                        default: 2010
        responses:
            200:
                data: properties
                description: listado de inmuebles filtrados
                schema:
                    id: data_properties_filter
                    properties:
                        data:
                            type: array
                            description: listado de inmuebles
                            items:
                                type: object
                                properties:
                                    id:
                                        type: integer
                                        description: id del inmueble
                                        default: 1
                                    description:
                                        type: string
                                        description: descripcion del inmueble
                                        default: Hermoso apartamento...
                                    status:
                                        type: string
                                        description: estado del inmueble
                                        default: en_venta
                                    city:
                                        type: string
                                        description: ciudad del inmueble
                                        default: bogota
                                    address:
                                        type: string
                                        description: direccion del inmueble
                                        default: cra 1 # 2 - 3
                                    price:
                                        type: integer
                                        description: precio del inmueble
                                        default: 1000000
                                    year:
                                        type: integer
                                        description: año de construccion del inmueble
                                        default: 2010
                        message:
                            type: string
                            description: status de la peticion
                            default: success
        """
        data = request.get_json()
        property_service = PropertyService()
        return Route.response(property_service.filter(data))