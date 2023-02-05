from models.model import Model
from models.schemas.property_schema import PropertySchema

class Property(Model):
    
    query = '''SELECT p.id, p.address, p.city, s.name as status, p.price, p.description
            FROM  property p
            join status_history sh on p.id =sh.property_id
            join status s on sh.status_id =s.id
            where (s.name = 'pre_venta' or s.name  = 'en_venta' or s.name = 'vendido') and p.price > 0 and p.address IS NOT NULL and p.city IS NOT NULL;
        '''

    # Get all properties from database
    def find_all(self):
        print("find_all")
        properties = self.get(self.query)
        for property in properties:
            yield PropertySchema(property)
