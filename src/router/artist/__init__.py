from fastapi import FastAPI, Header, HTTPException
import src.router.response.artist as response
import src.crud.artist as crud
from src.utils import auth_required

def rotas(app: FastAPI) -> None:

    @auth_required
    @app.get('/artist/', response_model=response.Create)
    def getArtist(name: str = None, artistID: str = None, authorization: str = Header(None)) -> dict:
        returnfunction:dict = {}
        if name is not None:
            returnfunction = crud.getArtistByName(name)

        elif id is not None:
            returnfunction = crud.getArtistByID(artistID)
        if returnfunction is not None:
            if not returnfunction["status"]:
                raise HTTPException(status_code=returnfunction["status_code"], detail=returnfunction["error"])
            return returnfunction


    @auth_required
    @app.get('/artist/{artistID}/lyrics', response_model=response.GetLyrics)
    def getArtistLyrics(artistID: str, authorization: str = Header(None)) -> dict:
        if artistID is None or artistID == "":
            raise HTTPException(
                status_code=400,
                detail="ID do artista nulo ou vazio!"
            )
        returnFunction = crud.getLyrics(artistID)
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction
    return

    @auth_required
    @app.get('/artist', response_model=response.GetArtists)
    def getArtists(authorization: str = Header()) -> dict:
        returnFunction = crud.getAllArtists()
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                response=returnFunction["error"]
            )
        return returnFunction
