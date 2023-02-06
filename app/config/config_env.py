from decouple import config


class ConfigEnv:
    mysql_host: str
    mysql_port: int
    mysql_user: str
    mysql_password: str
    mysql_db: str

    def __init__(self):
        self.load_env()

    # carga las variables de entorno
    def load_env(self):
        try:
            self.mysql_host = str(config("MYSQL_HOST"))
            self.mysql_port = int(config("MYSQL_PORT"))
            self.mysql_user = str(config("MYSQL_USER"))
            self.mysql_password = str(config("MYSQL_PASSWORD"))
            self.mysql_db = str(config("MYSQL_DB"))
        except Exception as e:
            print(e)
            print("Error al cargar las variables de entorno")
