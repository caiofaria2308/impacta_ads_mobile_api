from pydantic import BaseModel

class Artist(BaseModel):
    id: str
    name: str
    url: str
    pic_small: str
    pic_medium: str
    created_date: str


class Create(BaseModel):
    status: bool
    data: Artist