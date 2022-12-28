from dao.utility.db import MySql
from dto.Partecipation import Partecipation


class PartecipationDao:
    @classmethod
    def getAllPartecipations(cls):
        MySql.openConnection()
        MySql.query("select * from partecipazione")
        data = MySql.getResults()
        partecipation = []
        for element in data:
            partecipation.append(Partecipation(
                element[0], element[1], element[2], element[3], element[4]))
        return partecipation
