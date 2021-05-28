from fastapi import FastAPI

def rotas(app: FastAPI) -> None:
    @app.get('/users/')
    def getUsers() -> dict:
        return {}
    return
