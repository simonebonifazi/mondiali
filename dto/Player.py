class Player:
    def __init__(self,  ID,  nome):
        self._ID = ID
        self._nome = nome

    # getter

    @property
    def ID(self):
        return self._ID

    @property
    def nome(self):
        return self._nome

    # setter

    @ID.setter
    def ID(self,  ID):
        self._ID = ID

    @nome.setter
    def nome(self,  nome):
        self._nome = nome

    def __str__(self):

        return f"ID giocatore: {self._ID}, nome giocatore: {self._nome}"
