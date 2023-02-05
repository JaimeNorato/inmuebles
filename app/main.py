from flask import Flask,jsonify, request
from services.property_service import PropertyService

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'run server!'})

@app.route('/properties', methods=['GET'])
def properties():
    property_service = PropertyService()
    print(property_service)
    return jsonify({'data': property_service.get_all()})

@app.route('/properties', methods=['POST'])
def properties_filter():
    data = request.get_json()
    print(data)
    property_service = PropertyService()
    return jsonify({'data': property_service.filter(data)})
    

if __name__ == '__main__':
    app.run(debug=True)