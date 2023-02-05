from models.model import Model
from models.schemas.property_schema import PropertySchema

class Property(Model):
    
    query = '''SELECT p.id, p.address, p.city, s.name as status, p.price, p.description, p.`year`
            FROM  property p
            join status_history sh on p.id = sh.property_id
            join status s on sh.status_id = s.id
            where (s.name = 'pre_venta' or s.name  = 'en_venta' or s.name = 'vendido') and p.price > 0 and p.address IS NOT NULL and p.city IS NOT NULL
        '''

    # Get all properties from database
    def find_all(self):
        properties = self.get(self.query)
        for property in properties:
            yield PropertySchema(property)

    # Filter properties for city, status, year
    def filter(self, filters):
        self.apply_filters(filters)
        properties = self.get(self.query)
        for property in properties:
            yield PropertySchema(property)

    # Apply filters
    def apply_filters(self, filters):
        switch_filters = {
            "city": self.filter_city,
            "status": self.filter_status,
            "year": self.filter_year
        }

        for index, filter in filters.items():
            switch_filters.get(index, lambda filter: None)(filter)

    # Add filter of city
    def filter_city(self, city):
        self.query += f" and p.city = '{city}'"

    # Add filter of status
    def filter_status(self, status):
        self.query = self.query.replace("s.name = 'pre_venta' or s.name  = 'en_venta' or s.name = 'vendido'", f"s.name = '{status}'")

    # Add filter of year
    def filter_year(self, year):
        self.query += f" and p.year = {year}"