class Usuario:
    def __init__(self, nome, cpf, telefone, email, agencia, conta, saldo, chaves, id_usuario=None):
        self._id = id_usuario
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
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
    def cpf(self):
        return self._cpf
    
    @property
    def telefone(self):
        return self._telefone

    @property
    def email(self):
        return self._email

    @property
    def conta(self):
        return self._conta
    
    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @property
    def chave(self):
        return self._chaves
