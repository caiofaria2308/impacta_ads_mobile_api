from src.database import Database
from src.utils import gerarID
from multiprocessing import Process
import requests


def insertLyrics(lyrics: list, artist: str) -> None:
    for lyric in lyrics:
        print("inserindo em paralelo: %s" % lyric["desc"])
        sql = '''
            insert into artistLyrics (id, artist, name, url) values
            ("%s", "%s", "%s", "%s")
        '''
        parameters: tuple = (gerarID(), artist, lyric["desc"], lyric["url"])
        Database().executar(sql=sql, parameters=parameters, commit=True)


def getArtistVagalume(name: str) -> dict:
    link: str = f"https://www.vagalume.com.br/{name}/index.js"
    response = requests.get(link)
    if response.status_code != 200:
        return {
            "status": False,
            "error": "Não foi possível encontrar artista no Vagalume",
            "status_code": 404
        }
    artist: dict = response.json()["artist"]
    lyrics: dict = artist["lyrics"]["item"]
    sql: str = '''
    insert into artist (id, name, url, pic_small, pic_medium) values
    ("%s", "%s", "%s", "%s", "%s")
    '''
    parameters: tuple = (gerarID(), artist["desc"], artist["url"], artist["pic_small"], artist["pic_medium"])
    data: dict = Database().executar(sql=sql, parameters=parameters, commit=True)
    qtd: int = len(lyrics)
    for i in range(0, qtd, 50):
        if i == 0:
            step = 0
        else:
            step = i + 1
        p: Process = Process(target=insertLyrics, kwargs={"lyrics": lyrics[step: i+50], "artist": parameters[0]})
        p.start()
    sql: str = "select * from artist where id = '%s'" % parameters[0]
    data: dict = Database().executar(sql=sql)
    return data


def getArtistByName(name: str) -> dict:
    name_split = name.split(" ")
    name_formatted: str = ""
    for n in name_split:
        if name_formatted == "":
            name_formatted = f"{n}"
            continue
        name_formatted = f"{name_formatted}-{n}"
    sql: str = f"select * from artist where name like '{name}'"
    data: dict = Database().executar(sql=sql)
    if data["status"]:
        if len(data["data"]) == 0:
            data = getArtistVagalume(name_formatted)
        return {
            "status": True,
            "data": data["data"][0]
        }
    return data


def getArtistByID(id: str) -> dict:
    sql: str = " select * from artist where id = '%s'"
    parameters: tuple = (id,)
    data: dict = Database().executar(sql=sql, parameters=parameters)
    if data["status"]:
        return {
            "status": True,
            "data": data["data"][0]
        }
    return data


def getAllArtists() -> dict:
    sql: str = '''
        SELECT 
            a.id,
            a.name,
            a.url,
            a.pic_small,
            a.pic_medium,
            a.created_date
        FROM artist a
        ORDER BY name ASC
    '''
    artists: dict = Database().executar(sql=sql)
    if artists["status"]:
        for indice in range(len(artists["data"])):
            artist: dict = artists["data"][indice]
            sql: str = '''
                SELECT 
                    l.id,
                    l.name,
                    l.url
                FROM artistLyrics
                WHERE l.artist = '%s'
                ORDER BY name ASC
            '''
            parameters: list = [artist["id"]]
            lyrics: dict = Database().executar(sql=sql, parameters=parameters)
            if lyrics["status"]:
                artists["data"][indice]["lyrics"] = lyrics["data"]
            else:
                continue
    return artists


def getLyrics(artistID: str) -> dict:
    sql: str = '''
        select 
            l.id,
            a.id as artistID,
            a.name as artistName,
            a.url as artistUrl,
            a.pic_small as artistPic_small,
            a.pic_medium as artistPic_medium,
            a.created_date as artistCreated_date,
            l.name,
            l.url
        from artistLyrics l
        left join artist a on a.id = l.artist
        where a.id = '%s' 
    '''
    parameters: tuple = (artistID,)
    data: dict = Database().executar(sql=sql, parameters=parameters)
    return data
