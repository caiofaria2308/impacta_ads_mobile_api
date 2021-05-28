from uuid import uuid4
from functools import wraps
from config import Configuracao
import datetime
import jwt


def gerarID() -> str:
    """gerarID gera um GUID em formato str"""
    return str(uuid4())

def func_error():
    return {
        "status": False,
        "error": "Token inválido ou expirado"
    }


def auth_required(func) -> None:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if "authorization" not in kwargs or kwargs["authorization"] in (None, "", " "):
            return func_error()
        token_split = kwargs["authorization"].split(" ")
        conf = Configuracao()
        conf.carregar_config()
        try:
            token_decoded = jwt.decode(token_split[1], conf.secret, algorithms="HS256", options={"verify_exp": True})
        except:
            return func_error()

        return func(*args, **kwargs)
    return  wrapper