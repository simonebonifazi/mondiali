# tester
from dao.partecipationDao import PartecipationDao
from dao.organizationDao import OrganizationDao
from dao.playerDao import PlayerDao
from dao.teamDao import TeamDao
tester = PlayerDao.getPlayerWhoHadPlayedInThreeWorldCupOrInMoreThanOneTeam()
print(tester)
