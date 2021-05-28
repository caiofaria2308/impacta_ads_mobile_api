import src.router.user as routeruser
from fastapi import FastAPI


def rotas(app: FastAPI) -> None:
    routeruser.rotas(app)
