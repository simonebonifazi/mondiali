from dao.utility.db import MySql


class PartecipationDao:
    @classmethod
    def getAllPartecipations(cls):
        MySql.openConnection()
        MySql.query("select * from partecipazione")
        data = MySql.getResults()
        return data
