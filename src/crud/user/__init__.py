from src.database import Database
from config import Configuracao
from src.utils import gerarID
import hashlib
import src.router.request.user as userrequest
import jwt
import datetime


def login(form: userrequest.Login) -> bytes:
    sql = "select id, name, username, created_date from user where username = '%s' and password = '%s' "
    config = Configuracao()
    config.carregar_config()
    password = hashlib.sha224(str.encode(form.password)).hexdigest()
    password = hashlib.md5(str.encode(password)).hexdigest()
    parameters: tuple = (form.username, password)
    data = Database().executar(sql=sql, parameters=parameters)
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


def create(form: userrequest.Create):
    sql ='''
        insert into user(id, name, username, password) values
        ("%s", "%s", "%s", "%s")
    '''
    config = Configuracao()
    config.carregar_config()
    password = hashlib.sha224(str.encode(form.password)).hexdigest()
    password = hashlib.md5(str.encode(password)).hexdigest()
    parameters: tuple = (gerarID(), form.name, form.username, password)
    data = Database().executar(sql=sql, parameters=parameters, commit=True)
    if data['status']:
        sql = "select created_date from user where id = '%s'" % parameters[0]
        data = Database().executar(sql=sql)
        if data['status']:
            row = data['data'][0]
            print(data)
            return {
                "status": True,
                "data": {
                    "id": parameters[0],
                    "name": parameters[1],
                    "username": parameters[2],
                    "created_id": row["created_date"]
                }
            }
        print(data)
        return data
    print(data)
    return data
