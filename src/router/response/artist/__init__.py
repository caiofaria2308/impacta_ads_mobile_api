from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class Artist(BaseModel):
    id: str
    name: str
    url: str
    pic_small: str
    pic_medium: str
    created_date: datetime


class Lyrics(BaseModel):
    id: str
    artist: Artist
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



class Artists(BaseModel):
    id: str
    name: str
    url: str
    pic_small: str
    pic_medium: str
    created_date: datetime
    lyrics: List[Lyrics]


class GetArtists(BaseModel):
    status: bool
    error: Optional[str]
    status_Code: Optional[int]
    data: List[Artists]