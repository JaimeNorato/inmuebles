from models.model import Model


class PropertyService:
    def __init__(self, property_repository: Model):
        self.property_repository = property_repository

    def get_all(self):
        result = []
        properties = self.property_repository.find_all()
        for property in properties:
            result.append(property.__dict__)
        return result

    # Filter properties for address, city, status, price, description
    def filter(self, filters):
        result = []
        properties = self.property_repository.filter(filters)
        for property in properties:
            result.append(property.__dict__)
        return result
