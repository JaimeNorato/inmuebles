from config.database import DataBase


class Model:
    def __init__(self):
        self.db = DataBase()
        self.cursor = self.db.get_cursor()

    # executa el query
    def execute(self, query):
        try:
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    # obtiene todos los registros de la tabla
    def get(self, query):
        print("query")
        print(query)
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return False

    # obtiene un registro de la tabla
    def find(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            return False

    # actualiza un registro de la tabla
    def update(self, query):
        try:
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    # inserta un registro en la tabla
    def insert(self, query):
        try:
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    # elimina un registro de la tabla
    def delete(self, query):
        try:
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False
