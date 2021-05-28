from fastapi import FastAPI, Header
import src.router.response.artist as response
import src.crud.artist as crud
from src.utils import auth_required

def rotas(app: FastAPI) -> None:
    @auth_required
    @app.get('/artist/{name}')
    def getArtist(name: str, authorization: str = Header(None)) -> dict:
        return crud.getArtist(name)
    return
