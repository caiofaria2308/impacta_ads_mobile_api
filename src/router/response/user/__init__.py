from pydantic import BaseModel
from typing import Dict

class Login(BaseModel):
    token: str


class User(BaseModel):
    id: str
    name: str
    username: str
    created_date: str


class Create(BaseModel):
    status: bool
    data: User