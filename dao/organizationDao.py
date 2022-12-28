from dao.utility.db import MySql
from dto.Organization import Organization


class OrganizationDao:
    @classmethod
    def getAllOrganizations(cls):
        MySql.openConnection()
        MySql.query("select * from organizzazione")
        data = MySql.getResults()
        organizations = []
        for element in data:
            organizations.append(Organization(
                element[0], element[1]))
        return organizations
