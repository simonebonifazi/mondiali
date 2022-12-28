from dao.utility.db import MySql
from dto.Player import Player


class PlayerDao:
    @classmethod
    def getAllPlayers(cls):
        MySql.openConnection()
        MySql.query("select * from giocatore")
        data = MySql.getResults()
        players = []
        for element in data:
            players.append(Player(
                element[0], element[1]))
        return players

    @classmethod
    def getPlayerByID(cls, id):
        MySql.openConnection()
        MySql.query(f"select * from giocatore where ID = {id}")
        data = MySql.getResults()
        player = Player(data[0][0], data[0][1])
        return player

    @classmethod
    def getAllPlayerPerYear(cls, year):
        MySql.openConnection()
        MySql.query(
            f"SELECT * FROM mondiali.giocatore join partecipazione p on p.IDGiocatore where Anno = {year}")
        data = MySql.getResults()
        return data
