from pydantic import BaseModel


class PlayList(BaseModel):
    name: str


class PlayListSong(BaseModel):
    artistLyrics: str
