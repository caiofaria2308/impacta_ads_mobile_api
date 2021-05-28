from fastapi import FastAPI, Header
import src.crud.user as cruduser
import src.router.request as request
import src.router.response.user as responseuser


def rotas(app: FastAPI) -> None:
    @app.post('/login', response_model= responseuser.Login )
    def login(form: request.Login):
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
