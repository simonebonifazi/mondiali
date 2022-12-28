from dao.utility.db import MySql


class PlayerDao:
    @classmethod
    def getAllPlayers(cls):
        MySql.openConnection()
        MySql.query("select * from giocatore")
        data = MySql.getResults()
        return data

    @classmethod
    def getPlayerByID(cls, id):
        MySql.openConnection()
        MySql.query(f"select * from giocatore where ID = {id}")
        data = MySql.getResults()
        return data

    @classmethod
    def getAllPlayerPerYear(cls, year):
        MySql.openConnection()
        MySql.query(
            f"SELECT * FROM mondiali.giocatore join partecipazione p on p.IDGiocatore where Anno = {year}")
        data = MySql.getResults()
        return data
