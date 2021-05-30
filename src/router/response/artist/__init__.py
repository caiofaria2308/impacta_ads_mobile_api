from pydantic import BaseModel
from typing import Optional, List
import src.router.response.artist as respartist

class Artist(BaseModel):
    id: str
    name: str
    url: str
    pic_small: str
    pic_medium: str
    created_date: str


class Lyrics(BaseModel):
    id: str
    artist: respartist.Artist
    name: str
    url: str


class Create(BaseModel):
    status: bool
    data: Optional[Artist]
    error: Optional[str]
    status_code: Optional[int]


class GetLyrics(BaseModel):
    status: bool
    error: Optional[str]
    status_code: Optional[int]
    data: Optional[List[Lyrics]]