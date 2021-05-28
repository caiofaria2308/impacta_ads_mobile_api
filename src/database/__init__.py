import pymysql.cursors
from config import Configuracao

class Database:
    def __init__(self: object) -> None:
        return

    def conectar(self: object) -> pymysql.connect:
        conf = Configuracao()
        conf.carregar_config()
        try:
            connection = pymysql.connect(
                host=conf.database.host,
                user=conf.database.username,
                password=conf.database.password,
                db=conf.database.name,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
            return connection
        except Exception as error:
            print(error)
            return None
        return None


    def executar(self: object, sql: str="",parameters: tuple=(), **kwargs) -> dict:
        with self.conectar() as connection:
            if connection == None:
                return {
                    "status": False,
                    "error": "erro ao conectar com banco!"
                }
            with connection.cursor() as cursor:
                query = sql % parameters
                try:
                    cursor.execute(str(query))
                except Exception as err:
                    print(err)
                    return {
                        "status": False,
                        "error": "erro ao executar query!"
                    }
                if "commit" in kwargs and kwargs["commit"]:
                    connection.commit()
                    return {
                        "status": True,
                        "message": "Operação realizada com sucesso!"
                    }
                data = cursor.fetchall()
                data = {"status": True, "data": data}
                return data
