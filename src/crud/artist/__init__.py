from src.database import Database
from config import Configuracao
from src.utils import gerarID
import requests
from multiprocessing import Process

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
    link = f"https://www.vagalume.com.br/{name}/index.js"
    response = requests.get(link)
    print(link)
    if response.status_code != 200 :
        return {
            "status": False,
            "error": "Não foi possível encontrar artista no Vagalume"
        }
    artist = response.json()["artist"]
    lyrics = artist["lyrics"]["item"]
    sql = '''
    insert into artist (id, name, url, pic_small, pic_medium) values
    ("%s", "%s", "%s", "%s", "%s")
    '''
    parameters: tuple = (gerarID(), artist["desc"], artist["url"], artist["pic_small"], artist["pic_medium"])
    data = Database().executar(sql=sql % parameters, commit=True)
    qtd = len(lyrics)
    for i in range(0, qtd, 50):
        if i == 0:
            step = 0
        else:
            step = i + 1
        p = Process(target=insertLyrics, kwargs={"lyrics": lyrics[step: i+50], "artist": parameters[0]})
        p.start()
    sql = "select * from artist where id = '%s'" % parameters[0]
    data = Database().executar(sql=sql)
    data['data'] = data['data'][0]
    return data


def getArtist(name: str) -> dict:
    name_split = name.split(" ")
    name_formatted: str = ""
    for n in name_split:
        if name_formatted == "":
            name_formatted = f"{n}"
            continue
        name_formatted = f"{name_formatted}-{n}"
    sql = "select * from artist where name = '%s'" % name
    data = Database().executar(sql=sql)
    if data["status"]:
        if len(data["data"]) == 0:
            data = getArtistVagalume(name_formatted)
            return data
        return {
            "status": True,
            "data": data["data"][0]
        }
    return data
