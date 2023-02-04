import pymysql

class DataBase:

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # connect to database
    def connect(self):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database
        )
    
    # get cursor
    def get_cursor(self):
        return self.connect().cursor()
    
    # close connection
    def close(self):
        self.connect().close()