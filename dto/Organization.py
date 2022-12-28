class Employee:
    def __init__(self, anno, nazione):
        self.anno = anno
        self.nazione = nazione

    # getter

    @property
    def anno(self):
        return self._anno

    @property
    def nazione(self):
        return self._nazione

    # setter

    @anno.setter
    def anno(self, anno):
        self._anno = anno

    @nazione.setter
    def nazione(self, nazione):
        self._nazione = nazione

    def __str__(self):
        return f"Anno mondiale: {self._anno}, Nazione ospitante: {self._nazione}"
