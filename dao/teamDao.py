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

    @classmethod
    def getTeamWithMostPlayerConvocatedPerYear(cls):
        MySql.openConnection()
        MySql.query(
            "select count(*) as numeroConvocazioni, p.anno, p.nazione \
            from partecipazione p\
            group by p.nazione, p.anno\
            having count(*) >= any(select count(*)\
                                   from partecipazione p\
                                   where anno=p.anno\
                                   group by nazione) ")
        data = MySql.getResults()
        MySql.closeConnection()

        return data

    @classmethod
    def getAllNationWhoNeverWinWorldCupAtHomeEdition(cls):
        MySql.openConnection()
        MySql.query(
            "select o.nazione from organizzazione o  inner join squadra s on o.anno  where PosizioneInClassifica = 1 and o.nazione <> s.nazione")
        data = MySql.getResults()
        return data
