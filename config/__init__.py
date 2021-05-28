import json

class Database:
    """Database representa os dados para acessar o banco de dados"""
    def __init__(self: object) -> None:
        """Método construtor de Database"""
        self.__host: str = None
        self.__username: str = None
        self.__password: str = None
        self.__name: str = None
        return

    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, new_name: str) -> None:
        self.__name = new_name
        return

    @property
    def host(self: object) -> str:
        return self.__host

    @host.setter
    def host(self: object, new_host: str) -> None:
        self.__host = new_host
        return

    @property
    def username(self: object) -> str:
        return self.__username

    @username.setter
    def username(self: object, new_username: str) -> None:
        self.__username = new_username
        return

    @property
    def password(self: object) -> str:
        return self.__password

    @password.setter
    def password(self: object, new_password: str) -> None:
        self.__password = new_password
        return

    @property
    def dict(self: object) -> dict:
        """dict retorna um dicionário com todos os dados"""
        return {
            "host": self.__host,
            "name": self.__name,
            "username": self.__username,
            "password": self.__password
        }


class Configuracao:
    """Configuracao retorna todos os dados da config.json"""
    def __init__(self: object) -> None:
        self.__database: Database = None
        self.__secret: str = None
        return

    @property
    def database(self: object) -> Database:
        return self.__database

    @database.setter
    def database(self: object, new_database: Database) -> None:
        self.__database = new_database
        return

    @property
    def secret(self: object) -> str:
        return self.__secret

    @secret.setter
    def secret(self: object, new: str) -> None:
        self.__secret = new
        return


    def carregar_config(self: object) -> None:
        """carregar_config carrega os dados da config.json"""
        with open("config//config.json", "r") as file:
            file_dict = json.load(file)
            config_database = file_dict["database"]
            database = Database()
            database.name = config_database["name"]
            database.host = config_database["host"]
            database.username = config_database["username"]
            database.password = config_database["password"]
            self.database = database
            self.secret = file_dict["secret"]


    def dict(self: object) -> dict:
        """dict retorna um dicionário com todos os dados em formato dict"""
        return {
            "database": self.database.dict()
        }

