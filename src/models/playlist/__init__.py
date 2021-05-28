from datetime import datetime
from src.models.user import User
from src.models.artist import ArtistLyrics


class Playlist:
    def __init__(self: object) -> None:
        self.__id: str = None
        self.__user: User = None
        self.__name: str = None
        self.__created_date: datetime = None
        return

    @property
    def id(self: object) -> str:
        return self.__id

    @id.setter
    def id(self: object, new: str) -> None:
        self.__id = new
        return

    @property
    def user(self: object) -> User:
        return self.__user

    @user.setter
    def user(self: object, new: User) -> None:
        self.__user = new
        return

    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, new: str) -> None:
        self.__name = new
        return

    @property
    def created_date(self: object) -> datetime:
        return self.__created_date

    @created_date.setter
    def created_date(self: object, new: datetime) -> None:
        self.__created_date = new
        return


class PlaylistSong:
    def __init__(self: object) -> None:
        self.__id: str = None
        self.__playlist: Playlist = None
        self.__artistLyrics: ArtistLyrics = None
        return

    @property
    def id(self: object) -> str:
        return self.__id

    @id.setter
    def id(self: object, new: str) -> None:
        self.__id = new
        return

    @property
    def playlist(self: object) -> Playlist:
        return self.__playlist

    @playlist.setter
    def playlist(self: object, new: Playlist) -> None:
        self.__playlist = new
        return

    @property
    def artistLyrics(self: object) -> ArtistLyrics:
        return self.__artistLyrics

    @artistLyrics.setter
    def artistLyrics(self: object, new: ArtistLyrics) -> None:
        self.__artistLyrics = new
        return