class Team:
    def __init__(self, anno, nazione, allenatore, posizione_in_classifica):
        self.anno = anno
        self.nazione = nazione
        self.allenatore = allenatore
        self.posizione_in_classifica = posizione_in_classifica

    # getter
    @property
    def anno(self):
        return self._anno

    @property
    def nazione(self):
        return self._nazione

    @property
    def allenatore(self):
        return self._allenatore

    @property
    def posizione_in_classifica(self):
        return self._posizione_in_classifica

    # setter

    @anno.setter
    def anno(self, anno):
        self._anno = anno

    @nazione.setter
    def nazione(self, nazione):
        self._nazione = nazione

    @allenatore.setter
    def allenatore(self, allenatore):
        self._allenatore = allenatore

    @posizione_in_classifica.setter
    def posizione_in_classifica(self, posizione_in_classifica):
        self._posizione_in_classifica = posizione_in_classifica

    def __str__(self):
        return f"anno del mondiale: {self._anno}, nazione: {self._nazione}, allenatore: {self._allenatore}, rtanking: {self._posizione_in_classifica}"
