from model import Model

class Property(Model):
    
    query = '''SELECT p.id, p.address, p.city, s.name as status, p.price, p.description
            FROM  property p
            join status_history sh on p.id =sh.property_id
            join status s on sh.status_id =s.id
            where (s.name = 'pre_venta' or s.name  = 'en_venta' or s.name = 'vendido') and p.price > 0 and p.address IS NOT NULL and p.city IS NOT NULL;
        '''
    
    id = None
    address = None
    city = None
    status = None
    pice = None
    description = None

    def __init__(self, id, address, city, status, price, description):
        self.id = id
        self.address = address
        self.city = city
        self.status = status
        self.price = price
        self.description = description
    
    def find_all(self):
        properties = self.get(self.query)


        return PropertyModel.find_all()
