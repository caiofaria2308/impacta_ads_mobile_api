from fastapi import FastAPI, Header
from src.utils import auth_required
import src.crud.user as cruduser
import src.router.request.user as user
import src.router.response.user as responseuser


def rotas(app: FastAPI) -> None:
    @app.post('/login', response_model= responseuser.Login )
    def login(form: user.Login):
        login = cruduser.login(form)
        if login == b'Conexao':
            return {
                "error": "Erro ao conectar com banco de dados!"
            }
        elif login == b'Nenhum usuario':
            return {
                "error": "Usuário/senha incorretos!"
            }
        return {
            "token": login
        }

    @auth_required
    def create_user(form: user.Create, authorization: str = Header(None)):
        return cruduser.create(form)
