from fastapi import FastAPI, Header, HTTPException
import src.router.response.playlist as response
import src.router.request.playlist as playlistreq
import src.crud.playlist as crud
from src.utils import auth_required, authorizationDecrypt


def rotas(app: FastAPI) -> None:
    @auth_required
    @app.post("/playlist", response_model=response.CreateUpdateGetPlaylist)
    def createPlaylist(form: playlistreq.PlayList, authorization: str = Header(None)):
        decrypt = authorizationDecrypt(authorization)
        returnFunction = crud.insertPlayList(form=form, userID=decrypt["id"])
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction


    @auth_required
    @app.get("/playlist", response_model=response.GetAllPlaylist)
    def getPlayList(playlistID: str = None, authorization: str = Header(None)):
        decrypt = authorizationDecrypt(authorization)
        if playlistID is None:
            returnFunction = crud.getPlayLists(userID=decrypt["id"])
            if not returnFunction["status"]:
                raise HTTPException(
                    status_code=returnFunction["status_code"],
                    detail=returnFunction["error"]
                )
            return returnFunction
        returnFunction = crud.getPlayListByID(playlistID=playlistID, userID=decrypt["id"])
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction

    @auth_required
    @app.post("/playlist/lyrics", response_model=response.GetAllPlayListLyrics)
    def createPlaylistLyrics(playlistID: str = None, form: playlistreq.PlayListSong = None, authorization: str = Header(None)):
        if playlistID is None:
            raise HTTPException(
                status_code=400,
                detail="playlistID é um campo obrigatório!"
            )
        decrypt = authorizationDecrypt(authorization)
        form["playlistID"] = playlistID
        returnFunction = crud.insertPlayListLyrics(form=form, userID=decrypt["id"])
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction


    @auth_required
    @app.delete("/playlist/lyrics", response_model=response.Delete)
    def deletePlaylistLyrics(playlistLyricID: str = None, authorization: str = Header(None)):
        if playlistLyricID is None:
            raise HTTPException(
                status_code=400,
                detail="playlistLyricID é um campo obrigatório!"
            )
        decrypt = authorizationDecrypt(authorization)
        returnFunction = crud.deletePlayListLyrics(playlistLyricID=playlistLyricID, userID=decrypt["id"])
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction

    @auth_required
    @app.delete("/playlist", response_model=response.Delete)
    def deletePlaylist(playlistID: str = None, authorization: str = Header(None)):
        if playlistID is None:
            raise HTTPException(
                status_code=400,
                detail="playlistID é um campo obrigatório!"
            )
        decrypt = authorizationDecrypt(authorization)
        returnFunction = crud.deletePlayList(playlistID=playlistID, userID=decrypt["id"])
        if not returnFunction["status"]:
            raise HTTPException(
                status_code=returnFunction["status_code"],
                detail=returnFunction["error"]
            )
        return returnFunction
    return