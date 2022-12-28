from dao.utility.db import MySql


class PlayerDao:
    @classmethod
    def getAllPlayers(cls):
        MySql.openConnection()
        MySql.query("select * from giocatore")
        data = MySql.getResults()
        return data
