class Usuario:
    def __init__(self, nome, agencia, conta, saldo, chaves, id_usuario=None):
        self._id = id_usuario
        self._nome = nome
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo
        self._chaves = chaves

    @property
    def id_usuario(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def chave(self):
        return self._chaves
