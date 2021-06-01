from fastapi import FastAPI, Header, HTTPException
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


    @app.post('/user', response_model=responseuser.Create)
    def create_user(form: user.Create, authorization: str = Header(None)):
        returnFunction = cruduser.create(form)
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction


    @app.get('/')
    def index():
        return {
            "status": True
        }
