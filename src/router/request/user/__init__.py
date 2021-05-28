from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    username: str
    password: str


class Create(BaseModel):
    name: str
    username: str
    password: str
