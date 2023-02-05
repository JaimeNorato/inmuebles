from models.property import Property

class PropertyService:
    def __init__(self):
        self.property_repository = Property()

    def get_all(self):
        result = []
        properties = self.property_repository.find_all()
        for property in properties:
            result.append(property.__dict__)
        return result
    
    # Filter properties for address, city, status, price, description
    def filter(self, filters):
        result = []
        properties = self.property_repository.find_all()
        for property in properties:
            result.append(property.__dict__)
        return result

    # def get_by_id(self, id):
    #     return self.property_repository.get_by_id(id)

    # def create(self, property):
    #     return self.property_repository.create(property)

    # def update(self, id, property):
    #     return self.property_repository.update(id, property)

    # def delete(self, id):
    #     return self.property_repository.delete(id)