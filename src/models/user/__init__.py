from datetime import datetime

class User:
    def __init__(self: object) -> None:
        self.__id: str = None
        self.__name: str = None
        self.__username: str = None
        self.__password: str = None
        self.__created_date: datetime = None

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
    def username(self: object) -> str:
        return self.__username

    @username.setter
    def username(self: object, new: str) -> None:
        self.__username = new
        return

    @property
    def password(self: object) -> str:
        return self.__str

    @password.setter
    def password(self: object, new: str) -> None:
        self.__password = new
        return

    @property
    def created_date(self: object) -> datetime:
        return self.__created_date

    @created_date.setter
    def created_date(self: object, new: datetime) -> None:
        self.__created_date = new
        return
