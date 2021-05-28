from datetime import datetime

class Artist:
    def __init__(self: object) -> None:
        self.__id: str = None
        self.__name: str = None
        self.__url: str = None
        self.__pic_small: str = None
        self.__pic_medium: str = None
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
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, new: str) -> None:
        self.__name = new
        return

    @property
    def url(self: object) -> str:
        return self.__url

    @url.setter
    def url(self: object, new: str) -> None:
        self.__url = new
        return

    @property
    def pic_small(self: object) -> str:
        return self.__pic_small

    @pic_small.setter
    def pic_small(self: object, new: str) -> None:
        self.__pic_small = new
        return

    @property
    def pic_medium(self: object) -> str:
        return self.__pic_medium

    @pic_medium.setter
    def pic_medium(self: object, new: str) -> None:
        self.__pic_medium = new
        return

    @property
    def created_date(self: object) -> datetime:
        return self.__created_date

    @created_date.setter
    def created_date(self: object, new: datetime) -> None:
        self.__created_date = new
        return




class ArtistLyrics:
    def __init__(self: object) -> None:
        self.__id: str = None
        self.__artist: Artist = None
        self.__name: str = None
        self.__url: str = None
        return

    @property
    def id(self: object) -> str:
        return self.__id

    @id.setter
    def id(self: object, new: str) -> None:
        self.__id = new
        return

    @property
    def artist(self: object) -> Artist:
        return self.__artist

    @artist.setter
    def artist(self: object, new: Artist) -> None:
        self.__artist = new
        return

    @property
    def name(self: object) -> str:
        return self.__name

    @name.setter
    def name(self: object, new: str) -> None:
        self.__name = new
        return

    @property
    def url(self: object) -> str:
        return self.__url

    @url.setter
    def url(self: object, new: str) -> None:
        self.__url = new
        return