import pymysql
from config.config_env import ConfigEnv

class DataBase:

    def __init__(self):
        self.host = ConfigEnv().mysql_host
        self.port = ConfigEnv().mysql_port
        self.user = ConfigEnv().mysql_user
        self.password = ConfigEnv().mysql_password
        self.database = ConfigEnv().mysql_db

    # connect to database
    def connect(self):
        print("connect")
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