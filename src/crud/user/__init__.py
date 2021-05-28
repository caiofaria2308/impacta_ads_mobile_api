from src.database import Database
from config import Configuracao
import hashlib
import src.router.request as request
import jwt
import datetime


def login(form: request.Login) -> bytes:
    sql = "select id, name, username, created_date from user where username = '%s' and password = '%s' "
    config = Configuracao()
    config.carregar_config()
    password = hashlib.sha224(str.encode(form.password)).hexdigest()
    password = hashlib.md5(str.encode(password)).hexdigest()
    parameters: tuple = (form.username, password)
    data = Database.executar(self=Database, sql=sql, parameters=parameters)
    if data["status"]:
        if len(data["data"]) == 0:
            return bytes(b"Nenhum usuario")
        claims = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=8),
            "id": data["data"][0]["id"],
            "username": data["data"][0]["username"],
            "created_date":str(data["data"][0]["created_date"])
        }
        encode = jwt.encode(claims, config.secret, algorithm="HS256")
        return encode
    return bytes(b"None")
