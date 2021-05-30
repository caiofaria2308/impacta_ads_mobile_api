from pydantic import BaseModel
from typing import Optional, List
import src.router.response.artist as responseartist
import src.router.response.user as respuser
import datetime

class Playlist(BaseModel):
    id: str
    user: respuser.User
    name: str
    created_date: datetime.datetime


class PlayListLyrics(BaseModel):
    id: str
    playlist: Playlist
    artistLyrics: responseartist.Artist


class CreateUpdateGetPlaylist(BaseModel):
    status: bool
    data: Optional[Playlist]
    error: Optional[str]
    status_code: Optional[int]


class GetAllPlaylist(BaseModel):
    status: bool
    data: Optional[List[Playlist]]
    error: Optional[str]
    status_code: Optional[int]


class GetAllPlayListLyrics(BaseModel):
    status: bool
    data: Optional[List[PlayListLyrics]]
    error: Optional[str]
    status_code: Optional[int]


class Delete(BaseModel):
    status: bool
    error: Optional[str]
    status_code: Optional[int]
    message: Optional[str]


