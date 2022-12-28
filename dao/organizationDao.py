from dao.utility.db import MySql


class OrganizationDao:
    @classmethod
    def getAllOrganizations(cls):
        MySql.openConnection()
        MySql.query("select * from organizzazione")
        data = MySql.getResults()
        return data
