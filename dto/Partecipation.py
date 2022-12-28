
class Partecipation:
    def __init__(self, ID_giocatore, anno, nazione, ruolo, goal_segnati):
        self.ID_giocatore = ID_giocatore
        self.anno = anno
        self.nazione = nazione
        self.ruolo = ruolo
        self.goal_segnati = goal_segnati

    # getter
    @property
    def ID_giocatore(self):
        return self._ID_giocatore

    @property
    def anno(self):
        return self._anno

    @property
    def nazione(self):
        return self._nazione

    @property
    def ruolo(self):
        return self._ruolo

    @property
    def goal_segnati(self):
        return self._goal_segnati

    # setter

    @ID_giocatore.setter
    def ID_giocatore(self, ID_giocatore):
        self._ID_giocatore = ID_giocatore

    @anno.setter
    def anno(self, anno):
        self._anno = anno

    @nazione.setter
    def nazione(self, nazione):
        self._nazione = nazione

    @ruolo.setter
    def ruolo(self, ruolo):
        self._ruolo = ruolo

    @goal_segnati.setter
    def goal_segnati(self, goal_segnati):
        self._goal_segnati = goal_segnati

    def __str__(self):
        return f"identificativo giocatore : {self._ID_giocatore},anno del mondiale: {self._anno},nazione del giocatore: {self._nazione}, ruolo giocatore: {self._ruolo}, goal segnati dal giocatore: {self._goal_segnati}"
