class Transacao:
    def __init__(self, valor, data, origem, destino, status, id_transacao=None):
        self._id = id_transacao
        self._valor = valor
        self._data = data
        self._origem = origem
        self._destino = destino
        self._status = status

    @property
    def id_transacao(self):
        return self._id

    @property
    def valor(self):
        return self._valor

    @property
    def data(self):
        return self._data

    @property
    def origem(self):
        return self._origem

    @property
    def destino(self):
        return self._destino

    @property
    def status(self):
        return self._status
