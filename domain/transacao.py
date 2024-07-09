class Transacao:
    def __init__(self, valor, data, origem, destino, status, id_transacao = None):
        self._id = id_transacao
        self._valor = valor
        self._data = data
        self._origem = origem
        self.destino = destino
        self.status = status