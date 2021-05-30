from src.database import Database
from src.utils import gerarID
import src.models.playlist as model
import src.router.request.playlist as request

def insertPlayList(form: request.PlayList, userID: str) -> dict:
    sql: str = "insert into playlist (id, user, name) values( '%s', '%s', '%s)'"
    parameters: tuple = (gerarID(), userID, form.name)
    data = Database().executar(sql=sql, parameters=parameters, commit=True)
    if data["status"]:
        return getPlayListByID(playlistID=parameters[0], userID=userID)
    return data


def getPlayLists(userID: str) -> dict:
    sql: str = '''
            select
            p.id,
            json_object("id", u.id, "name", u.name, "username", u.username, "created_date", u.created_date) as user,
            p.name,
            p.created_date 
            from playlist p where u.id = "%s"
            left join user u on u.id = p.user  
    '''
    parameters: list = [userID]
    data = Database().executar(sql=sql, parameters=parameters)
    return data


def getPlayListByID(playlistID: str, userID: str) -> dict:
    sql: str = '''
                select
                p.id,
                json_object("id", u.id, "name", u.name, "username", u.username, "created_date", u.created_date) as user,
                p.name,
                p.created_date 
                from playlist p where p.id = "%s" and u.id = %s
                left join user u on u.id = p.user  
        '''
    parameters: tuple = (playlistID, userID)
    data = Database().executar(sql=sql, parameters=parameters)
    if data["status"]:
        if len(data["data"]) == 0:
            return data
        return {
            "status": data["status"],
            "data": data["data"][0]
        }
    return data


def insertPlayListLyrics(form: request.PlayListSong, userID: str) -> dict:
    sql = '''
        insert into playlistLyrics (id, playlist, artistLyrics)
        values ('%s', '%s', '%s')
    '''
    parameters: tuple = (gerarID(), form["playlistID"], form["artistLyrics"])
    data = Database().executar(sql=sql, parameters=parameters, commit=True)
    if data["status"]:
        data = Database().executar(
            sql="select * from playlistLyrics where id = '%s'",
            parameters=[parameters[0]]
        )
        if data["status"]:
            return {
                "status": data["status"],
                "data": data["data"][0]
            }
    return data


def deletePlayListLyrics(playlistLyricID: str, userID: str) -> dict:
    sql = '''
    delete from playlistLyrics where id = '%s'
    '''
    parameters: list = [playlistLyricID]
    data = Database().executar(sql=sql, parameters=parameters, commit=True)
    data["message"] = "Música da playlist foi deletada com sucesso!"
    return data


def deletePlayList(playlistID: str, userID: str) -> dict:
    sql = '''
        delete from playlist where id = '%s'
        '''
    parameters: list = [playlistID]
    data = Database().executar(sql=sql, parameters=parameters, commit=True)
    data["message"] = "Playlist deletada com sucesso!"
    return data
