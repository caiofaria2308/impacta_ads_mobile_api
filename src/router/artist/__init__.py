from fastapi import FastAPI, Header, HTTPException
import src.router.response.artist as response
import src.crud.artist as crud
from src.utils import auth_required

def rotas(app: FastAPI) -> None:
    @auth_required
    @app.get('/artist/', response_model=response.Create)
    def getArtist(name: str = None, artistID: str = None, authorization: str = Header(None)) -> dict:
        returnfunction = None
        if name is not None:
            returnfunction = crud.getArtistByName(name)
        elif id is not None:
            returnfunction = crud.getArtistByID(artistID)
        if returnfunction is not None:
            if not returnfunction["status"]:
                return HTTPException(status_code=retorno["status_code"], detail=retorno["error"])
            return returnfunction


    @auth_required
    @app.get('/artist/{artistID}/lyrics', response_model=response.GetLyrics)
    def getArtistLyrics(artistID: str, authorization: str = Header(None)) -> dict:
        if artistID is None or artistID == "":
            return HTTPException(
                status_code=400,
                detail="ID do artista nulo ou vazio!"
            )
        returnFunction = crud.getLyrics(artistID)
        if not returnFunction["status"]:
            return HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction
    return
