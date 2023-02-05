class PropertySchema:
    id: int
    address: str
    city = str
    status = str
    pice = str
    description = str

    def __init__(self, property):
        self.fill(property)

    # fill property object
    def fill(self, property):
        self.id = int(property[0])
        self.address = property[1]
        self.city = property[2]
        self.status = property[3]
        self.price = property[4]
        self.description = property[5]
        return self

    def __str__(self):
        return f'Property: {self.id}, {self.address}, {self.city}, {self.status}, {self.price}, {self.description}'