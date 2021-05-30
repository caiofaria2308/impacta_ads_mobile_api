from pydantic import BaseModel
from typing import Dict, Optional

class Login(BaseModel):
    token: str


class User(BaseModel):
    id: str
    name: str
    username: str
    created_date: str


class Create(BaseModel):
    status: bool
    data: Optional[User]
    error: Optional[str]
    status_code: Optional[int]