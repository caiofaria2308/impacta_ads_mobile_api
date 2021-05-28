from pydantic import BaseModel

class Login(BaseModel):
    token: str