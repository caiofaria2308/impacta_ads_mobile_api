import src.router.user as routeruser
import src.router.artist as routerartist
from fastapi import FastAPI


def rotas(app: FastAPI) -> None:
    routeruser.rotas(app)
    routerartist.rotas(app)
