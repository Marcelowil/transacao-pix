class Usuario:
    def __init__(self, nome, agencia, conta, saldo, chaves, id_usuario = None):
        self._id = id_usuario
        self._nome = nome
        self._agencia = agencia
        self._conta = conta
        self.saldo = saldo
        self._chaves = chaves

    