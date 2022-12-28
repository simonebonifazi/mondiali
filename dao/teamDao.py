from dao.utility.db import MySql


class TeamDao:

    @classmethod
    def getAllTeams(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM squadra")
        data = MySql.getResults()
        MySql.closeConnection()
        return data

    @classmethod
    def getTeamByTopThreePlacement(cls):
        MySql.openConnection()
        MySql.query(
            "SELECT * FROM mondiali.squadra where PosizioneInClassifica <= 3")
        data = MySql.getResults()
        MySql.closeConnection()

        return data
